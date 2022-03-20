import os

from axyutils.file_io import atomic_write

class MakeNginxConfig:
    '''
    NGINX config generator
    '''
    def make(self):
        '''
        Assume NGINX configuration consists of main template and per-server template.
        Main template defines some globals such as upstreams,
        whereas per-server template defines server-specific configuration.
        '''
        print('Generating', self.make_name)
        component_conf = self.component_conf.copy()
        output_file = component_conf.pop('dest')
        main_template_class = self.classes[component_conf.pop('main_template')]
        main_template = main_template_class()
        server_template_class = self.classes[component_conf.pop('server_template')]
        server_template = server_template_class()
        servers = component_conf.pop('servers')

        # make root_dir absolute
        # XXX depends on current directory
        component_conf['root_dir'] = os.path.abspath(component_conf['root_dir'])

        # render per-server configuration
        servers_conf = []
        all_langs = [lang for lang, locale in self.lang_locales]
        all_langs_regexp = f"({'|'.join(all_langs)})"  # XXX how about locales?
        for hostname in servers:
            servers_conf.append(server_template.render(
                hostname = hostname,
                all_langs = all_langs,
                all_langs_regexp = all_langs_regexp,
                canonical_lang = all_langs[0],
                default_lang = self.default_language,
                **component_conf
            )['content'])
        servers_conf = '\n'.join(servers_conf)

        # render main configuration
        nginx_config = main_template.render(
            servers_conf = servers_conf,
            **component_conf
        )['content']

        atomic_write(nginx_config, output_file, encoding='utf-8')
