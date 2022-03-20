from clabate import Template, indented

import idna

class NginxConfig(Template):

    content = indented(0, '''
        {servers_conf}
    ''')

class ServerConfig(Template):

    content = indented(0, '''
        {main_config}
        {production_specific_config}
    ''')

    @property
    def idna_hostname(self, context):
        return idna.encode(context['hostname']).decode('ascii')

    schema = 'https'

    listen = indented(4, '''
        listen 443 ssl;
        ssl_certificate /etc/nginx/certificates/{idna_hostname}.crt;
        ssl_certificate_key /etc/nginx/certificates/{idna_hostname}.key;
    ''')

    main_config = indented(0, '''
        server {{
            {listen}

            server_name {idna_hostname};

            {set_lang}

            root {root_dir}/{hostname};

            location = / {{
                # this will be processed in the next "location /" as /index.html
                index /index;
            }}

            location / {{
                {sanitize}

                # check precompressed files
                gzip_static on;

                try_files /www-data$uri /content$uri /content$uri.html =404;
            }}

            location /static {{
                root {root_dir};
                {sanitize}
                try_files $uri =404;
            }}

            {status_pages}
        }}

        server {{
            # Redirect *.{idna_hostname} to canonical {idna_hostname}
            {listen}

            server_name *.{idna_hostname};

            {set_lang}
            {permanent_redirect}
        }}
    ''')

    production_specific_config = indented(0, '''
        server {{
            # redirect HTTP to HTTPS except /.well-known
            listen 80;
            server_name {idna_hostname} *.{idna_hostname};

            root {root_dir}/{hostname};

            location /.well-known {{
                try_files $uri =404;
            }}

            {set_lang}
            {permanent_redirect}
        }}
    ''')

    sanitize = indented(8, '''
                if ($request_method != GET) {{
                    return 406;
                }}

                # strip query string
                if ($args) {{
                    rewrite ^ $uri? permanent;
                }}

                # tell the browser to revalidate content each time the page is requested
                add_header Cache-Control "must-revalidate";
    ''')

    permanent_redirect = indented(4, '''
            location / {{
                if ($request_method != GET) {{
                    return 406;
                }}
                return 301 {schema}://{idna_hostname}$uri;
            }}

            {status_pages}
    ''')

# XXX locale?           if ($http_accept_language ~* '^(.+?),') {{
    set_lang = indented(4, '''
            set $lang 'en';
            if ($http_accept_language ~* '^(..).*?,') {{
                set $lang $1;
            }}
            if ($lang !~* '{all_langs_regexp}') {{
                set $lang '{canonical_lang}';
            }}
            if ($lang ~* '{default_lang}') {{
                set $lang '';
            }}
    ''')

    status_pages = indented(4, '''
            location /status-pages {{
                # avoid internal redirect to / location again
                root {root_dir}/{hostname};

                # check precompressed files
                gzip_static on;
            }}
            error_page 403 /status-pages/$lang/403.html;
            error_page 404 410 /status-pages/$lang/404.html;
            error_page 406 =403 /status-pages/access_denied.json;
            error_page 500 501 502 503 504 505 506 507 508 509 510 511 /status-pages/$lang/50x.html;
    ''')
