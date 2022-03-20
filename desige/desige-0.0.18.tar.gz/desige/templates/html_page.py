'''
Basic HTML page templatee.

:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

from clabate import MinifiedMarkupTemplate, Markup, TagAttr

class HTMLPageTemplate(MinifiedMarkupTemplate):

    html = Markup('''
        <!DOCTYPE html>
        <html lang="{lang}">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            {favicon}
            {html_head}
        </head>
        <body{body_attributes}>
            {header}
            <main{main_attributes}>
                {content}
            </main>
            {footer}
        </body>
        </html>
    ''')

    lang = 'en'

    favicon = Markup('<link rel="shortcut icon" href="/favicon.ico">')

    html_head = Markup('''
        {head_title}
        {stylesheet}
    ''')

    head_title = Markup('<title>{site_name}</title>')

    site_name = 'My Web Site'

    stylesheet = ''

    body_attributes = ''
    main_attributes = ''

    header = ''
    footer = ''
