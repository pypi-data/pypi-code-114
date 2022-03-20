'''
Basic page.

:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

from datetime import datetime
import os

from axyutils.file_io import atomic_write_with_gz
import yaml


class BasicPage:
    '''
    Page data stored on disk.
    This base class implements metadata loading and provides a few other methods.
    '''

    def __init__(self, metadata_filename, template, src_path):
        self.metadata_filename = metadata_filename
        self.template = template
        self.src_path = src_path
        self.load_metadata()

    @classmethod
    def load_class_def(self, metadata_filename):
        with open(metadata_filename, 'r', encoding='utf-8') as f:
            docs = yaml.safe_load_all(f)
            return next(docs)  # first doc is the page class definition

    @classmethod
    def is_page_entry(cls, scandir_entry):
        '''
        Check if scandir_entry is a page data (metadata yaml file or a directory containing page data).
        '''
        return scandir_entry.is_file() and scandir_entry.name.endswith('.yaml')

    @classmethod
    def make_metadata_filename(cls, src_path):
        return src_path

    def load_metadata(self):
        '''
        Load page metadata.
        '''
        with open(self.metadata_filename, 'r', encoding='utf-8') as f:
            docs = yaml.safe_load_all(f)
            next(docs)  # skip page class definition
            self.metadata = next(docs)

    def localize_strings(self, data, lang):
        '''
        Replace all dicts that contain language codes with localized values.
        Use for metadata localization.
        '''
        def process_dict(src):
            dest = dict()
            for k, v in src.items():
                if isinstance(v, dict):
                    if lang in v:
                        dest[k] = v[lang] or ''
                    else:
                        dest[k] = process_dict(v)
                elif isinstance(v, list):
                    dest[k] = process_list(v)
                else:
                    dest[k] = v
            return dest

        def process_list(src):
            dest = []
            for v in src:
                if isinstance(v, dict):
                    if lang in v:
                        dest.append(v[lang] or '')
                    else:
                        dest.append(process_dict(v))
                elif isinstance(v, list):
                    dest.append(process_list(v))
                else:
                    dest.append(v)
            return dest

        return process_dict(data)

    def get_date_modified(self):
        '''
        Get page modification date/time.
        '''
        timestamp = os.path.getmtime(self.metadata_filename)
        return datetime.utcfromtimestamp(timestamp)

    def needs_rendering(self, layout):
        '''
        Check if a page is stale and needs rendering.
        '''
        if not os.path.exists(layout.filename):
            return True
        output_filetime = datetime.utcfromtimestamp(os.path.getmtime(layout.filename))
        return self.get_date_modified() > output_filetime

    def render(self, layout, **kwargs):
        '''
        Render status page and write on disk.
        '''
        rendering_params = dict(
            layout = layout,
            metadata = self.localize_strings(self.metadata, layout.lang),
            **kwargs
        )
        context = self.template.render(**rendering_params)
        self.validate(context['html'])

        atomic_write_with_gz(context['html'], layout.filename, encoding='utf-8')
        return context

    def validate(self, markup):
        '''
        Basic abstract method does nothing.
        '''
        pass


class PagesDirectory:
    '''
    Iteration interface for pages stored in a filesystem.
    '''

    def __init__(self, source_dir, page_classes):
        self.source_dir = source_dir
        self.page_classes = page_classes
        # because all page classes are of the same kind,
        # get any class to process entries
        self._page_class = list(page_classes.values())[0]['page']

    def instantiate_page(self, metadata_filename, src_path):
        '''
        Load page class name from metadata (first doc in the stream)
        and create an instance of that class.
        '''
        class_def = self._page_class.load_class_def(metadata_filename)
        page_class_name = class_def['page_class']
        if page_class_name not in self.page_classes:
            raise Exception(f'Page class {page_class_name} not defined')

        page_class = self.page_classes[page_class_name]
        template = page_class['template']()
        return page_class['page'](metadata_filename, template, src_path)

    def __iter__(self):
        '''
        Initialize pages iterator.
        '''
        # currently scanned path, a list of directory names
        self._iter_path = []

        # stack of directory scanners that match _iter_path
        # plus root directory scanner in the very beginning:
        self._iter_stack = [
            os.scandir(self.source_dir)
        ]
        return self

    def __next__(self):
        '''
        Iterate pages.

        Returns:
            an instance of WebPage class or subclass
        '''
        while True:
            # this outer loop is for managing self._iter_stack
            try:
                while True:
                    # this inner loop is for skipping unwanted entries
                    entry = next(self._iter_stack[-1])
                    if entry.is_dir():
                        self._iter_path.append(entry.name)

                    if self._page_class.is_page_entry(entry):
                        metadata_filename = self._page_class.make_metadata_filename(entry.path)
                        return self.instantiate_page(
                            metadata_filename,
                            (self.source_dir, *self._iter_path, entry.name)
                        )

                    if entry.is_dir():
                        # start new recursion level
                        subdirectory = os.path.join(self.source_dir, *self._iter_path)
                        self._iter_stack.append(
                            os.scandir(subdirectory)
                        )
                        # get next entry on the next iteration of the outer loop
                        break

            except StopIteration:
                # close scandir iterator
                scandir = self._iter_stack.pop()
                scandir.close()
                if len(self._iter_stack) == 0:
                    # top-level iteration complete
                    raise
                else:
                    # return to previous recursion level
                    self._iter_path.pop()
