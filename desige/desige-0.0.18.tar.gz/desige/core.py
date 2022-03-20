'''
Desige: declassed site generator.

Modular generator with the ability to easily replace components, including base classes.
No strict class hierarchy, therefore.

:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

from importlib import import_module
import inspect
import os
import shutil
import types

from axyutils.file_io import atomic_write, atomic_write_with_gz
from clabate import Markup
import yaml

class SiteGenerator:

    def __init__(self, config):
        self.config = config
        self.classes = ClassBuilder(config.classes)
        self._set_languages(config)
        self.components = self._process_components_config(config)
        return

    def _set_languages(self, config):
        # set language attributes based on config settings
        self.default_language = config.default_language
        self.lang_locales = config.languages

    def _process_components_config(self, config):
        # process components configuration
        components = dict()
        for c_name, c_conf in config.components.items():
            if 'make' not in c_conf:
                continue
            # get make class
            c_conf['make'] = self.classes[c_conf['make']]
            # make subset of servers
            if 'servers' in c_conf:
                c_conf['servers'] = list(set(c_conf['servers']) & set(config.servers))
            else:
                c_conf['servers'] = config.servers
            components[c_name] = c_conf
        return components

    def make(self, **rendering_params):
        '''
        Simple make system.
        '''
        prepare_methods = []
        make_methods = []
        finalize_methods = []
        for c_name, c_conf in self.components.items():
            c_conf = c_conf.copy()
            make_class = c_conf.pop('make')
            make = make_class(
                c_name,
                self.config.servers,
                self.lang_locales,
                self.default_language,
                self.classes,
                c_conf,
                rendering_params
            )
            prepare_methods.append(make.prepare)
            make_methods.append(make.make)
            finalize_methods.append(make.finalize)

        # call methods
        for method in prepare_methods:
            method()
        for method in make_methods:
            method()
        for method in finalize_methods:
            method()

class ClassBuilder:
    '''
    Helper class to construct classes and access them by name.
    '''
    def __init__(self, class_defs):
        self._classes = dict()
        for class_name, subclass_names in class_defs.items():
            subclasses = tuple(self[subclass_name] for subclass_name in subclass_names[::-1])
            cls = type(class_name, subclasses, {})
            self._classes[class_name] = cls

    def __getitem__(self, class_name):
        if class_name in self._classes:
            return self._classes[class_name]
        else:
            # try to import the module
            module_name, class_name = class_name.rsplit('.', 1)
            module = import_module(module_name)
            # get class_name from the module
            return getattr(module, class_name)

class MakeBase:

    def __init__(self,
                make_name,
                servers,
                lang_locales,
                default_language,
                classes,
                component_conf,
                rendering_params
            ):
        self.make_name = make_name
        self.servers = servers
        self.lang_locales = lang_locales
        self.default_language = default_language
        self.classes = classes
        self.component_conf = component_conf
        self.rendering_params = rendering_params

    def prepare(self):
        pass

    def make(self):
        pass

    def finalize(self):
        pass

    def expand_dest(self):
        '''
        Expand dest parameter.
        '''
        if '{server}' in self.component_conf['dest']:
            for server in self.servers:
                yield server, self.component_conf['dest'].format(server=server)
        else:
            yield '', self.component_conf['dest']

class CopyTree(MakeBase):

    def make(self):
        for server, dest_dir in self.expand_dest():
            print('Copying', self.make_name, 'from', self.component_conf['src'], 'to', dest_dir)
            shutil.copytree(
                self.component_conf['src'],
                dest_dir,
                dirs_exist_ok=True
            )

class MakePages(MakeBase):

    def make(self):
        from .layouts import Layouts
        page_classes = self._make_page_classes()
        page_iterator_class = self.classes[self.component_conf['iterator']]
        layout_class = self.classes[self.component_conf['layout']]
        src_path = self.component_conf['src']
        pages = page_iterator_class(src_path, page_classes)
        for page in pages:
            for server in self.servers:
                layouts = Layouts(layout_class, server, page,
                                  self.lang_locales, self.default_language, self.component_conf)
                for layout in layouts:
                    self.render_page(page, layout)

    def render_page(self, page, layout):
        if page.needs_rendering(layout):
            print(f"Rendering {layout.filename}")
            page.render(layout, **self.rendering_params)
        else:
            print(f"Skipping {layout.filename}")

    def _make_page_classes(self):
        # resolve class names
        page_classes = dict()
        for page_class_name, page_class in self.component_conf['page_classes'].items():
            page_classes[page_class_name] = dict(
                page = self.classes[page_class['page']],
                template = self.classes[page_class['template']]
            )
        return page_classes

class MakeSitemap:

    def finalize(self):
        '''
        Concatenate all sitemap entry files from sitemap cache.
        '''
        super().finalize()

        print('Generating sitemap')

        from .templates import SitemapTemplate

        # recursive collector
        def collect_sitemap_entries(server, path_components, sitemap_entries):
            src_directory = os.path.join(self.component_conf['sitemap_cache_dir'].format(server=server), *path_components)
            if os.path.exists(src_directory):
                with os.scandir(src_directory) as entries:
                    for entry in entries:
                        if entry.is_file():
                            with open(entry.path, 'r', encoding='utf-8') as f:
                                sitemap_entries.append(f.read())
                        elif entry.is_dir():
                            collect_sitemap_entries(server, path_components + [entry.name], sitemap_entries)

        for server, dest_dir in self.expand_dest():
            sitemap_entries = []
            collect_sitemap_entries(server, [], sitemap_entries)

            sitemap_xml = SitemapTemplate().render(
                entries=Markup(''.join(sitemap_entries)),
                **self.rendering_params
            )['xml']

            output_filename = os.path.join(self.component_conf['sitemap_dest_dir'].format(server=server), 'sitemap.xml')
            atomic_write_with_gz(sitemap_xml, output_filename, encoding='utf-8')
