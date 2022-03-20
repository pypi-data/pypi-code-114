'''
Layout establishes relation between output directories/pages and their URLs.

'''

import os

class Layouts:
    '''
    Create and iterate layouts.

    Canonical layout is the first layout, for the first language in the list.
    '''

    # XXX fix args
    def __init__(self, layout_class, server, page, lang_locales, default_language, component_config):
        self.layouts = [layout_class(server, page, lang, locale, default_language, component_config)
                        for lang, locale in lang_locales]
        self.layouts[0].canonical = True
        for layout in self.layouts[1:]:
            layout.canonical = False
        for i, layout in enumerate(self.layouts):
            layout.alternate = self.layouts[:i] + self.layouts[i+1:]

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.layouts):
            raise StopIteration
        layout = self.layouts[self._iter_index]
        self._iter_index += 1
        return layout

class BasicLayout:
    '''
    XXX
    '''
    def __init__(self, server, page, lang, locale, default_language, component_config):
        self.server = server.rstrip('/')
        self.page = page
        self.path = page.src_path[1:]
        self.lang = lang
        self.default_language = default_language
        self.locale = locale
        self.component_config = component_config

        self.make_path_lang()
        self.make_url_path()
        self.make_url()
        self.make_filename()

    def __del__(self):
        # break cyclic references
        delattr(self, 'alternate')

    def make_path_lang(self):
        if self.lang == self.default_language:
            # omit lang if specified as default language
            self.path_lang = None
        else:
            self.path_lang = lang

    def make_url_path(self):
        self.url_path = []
        if self.path_lang:
            self.url_path.append(self.path_lang)
        self.url_path.extend(self.path)

    def make_url(self):
        '''
        Make layout components.
        '''
        # XXX make schema configurable
        if self.page.metadata.get('is_index', False):
            # cut last path component for index page
            path = self.url_path[:-1]
        else:
            path = self.url_path
        self.uri = f"/{'/'.join(path)}"
        self.url = f"https://{self.server}{self.uri.rstrip('/')}"

    def make_filename(self):
        '''
        This sets basic filename.
        Subclasses need to override this method.
        '''
        filename = self.make_dest_path(self.component_config['dest'], self.url_path)
        self.filename = os.path.splitext(filename)[0] + '.html'

    def make_dest_path(self, base_dir, relative_path):
        '''
        Expand {server} in the `base_dir` and join with `relative_path`.
        '''
        absolute_path = [base_dir.format(server=self.server)]
        absolute_path.extend(relative_path)
        return os.path.join(*absolute_path)


class StatusPagesLayout:

    def make_url_path(self):
        # status pages are not hierarchial, drop path components
        # and leave the last one, filename only
        self.url_path = self.path[-1:]
