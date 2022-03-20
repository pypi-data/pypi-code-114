'''
WebPage and directory iterator.

:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

from datetime import datetime
import os

from axyutils.file_io import atomic_write, atomic_write_with_gz
from clabate import Markup
import dateutil.parser

from . import PagesDirectory

class WebPage:
    '''
    Web page data stored on disk.

    Ancestor: BasicPage.
    '''

    @classmethod
    def is_page_entry(cls, scandir_entry):
        '''
        Check if scandir_entry contains page data by checking existence of metadata YAML file.
        '''
        return scandir_entry.is_dir() and os.path.exists(cls.make_metadata_filename(scandir_entry.path))

    @classmethod
    def make_metadata_filename(cls, src_dir):
        return os.path.join(src_dir, os.path.basename(src_dir) + '.yaml')

    def make_content_filename(self, lang):
        return f'{os.path.join(*self.src_path)}.{lang}.html'

    def load_metadata(self):
        '''
        Load and preprocess page metadata.
        '''
        super().load_metadata()
        self.preprocess_date_created()
        self.set_date_modified()
        self.preprocess_metadata()

    def preprocess_date_created(self):
        self.metadata['date_created'] = dateutil.parser.parse(self.metadata['date_created'])

    def set_date_modified(self):
        self.metadata['date_modified'] = self.get_date_modified()

    def preprocess_metadata(self):
        '''
        Basic metadata preprocessing.
        '''
        pass

    def get_date_modified(self):
        '''
        Get page modification date/time.
        '''
        dates = []
        with os.scandir(os.path.join(*self.src_path[:-1])) as entries:
            for entry in entries:
                if entry.is_file():
                    dates.append(entry.stat().st_mtime)
        if len(dates) == 0:
            return None
        else:
            return datetime.utcfromtimestamp(max(dates))

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
        Render page template and save output files.
        '''
        rendering_params = dict(
            layout = layout,
            metadata = self.localize_strings(self.metadata, layout.lang),
            content = Markup(self.load_content(layout.lang)),
            **kwargs
        )
        self.make_og_images(rendering_params)
        self.make_twitter_images(rendering_params)

        context = self.template.render(**rendering_params)
        self.validate(context['html'])
        atomic_write_with_gz(context['html'], layout.filename, encoding='utf-8')

        return context

    def load_content(self, lang):
        '''
        Load HTML content.
        '''
        content_filename = self.make_content_filename(lang)
        if os.path.exists(content_filename):
            with open(content_filename, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return ''

    def make_og_images(self, rendering_params):
        pass

    def make_twitter_images(self, rendering_params):
        pass


class WebPagesLayout:

    def make_url_path(self):
        super().make_url_path()
        # delete last component from url_path because it's a path to the metadata file
        del self.url_path[-1]
