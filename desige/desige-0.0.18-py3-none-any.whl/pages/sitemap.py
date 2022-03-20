import os

from axyutils.file_io import atomic_write

class SitemapEntry:
    '''
    Add sitemap entry to a page.
    '''

    def render(self, layout, **kwargs):
        context = super().render(layout, **kwargs)
        if layout.canonical:
            if self.metadata.get('sitemap', False):
                atomic_write(context['sitemap_entry'], layout.sitemap_entry_filename, encoding='utf-8')

class SitemapLayout:

    def make_filename(self):
        '''
        Extend base method to make filename for sitemap entry.
        '''
        super().make_filename()
        self.sitemap_entry_filename = self.make_dest_path(
            self.component_config['sitemap_cache_dir'],
            self.path  # use self.path, don't need lang in the path as in self.url_path
        ) + '.xml'
