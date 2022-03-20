'''
Error page template.

:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

from clabate import Markup

class ErrorPageTemplate:

    head_title = Markup('<title>{metadata[title]} | {site_name}</title>')

    content = Markup('''
        <div class="error">
            <div class="header">{metadata[header]}</div>
            {description_html}
        </div>
    ''')

    @property
    def description_html(self, context):
        description = context['metadata']['description']
        if description:
            return Markup(f"<div class=\"description\">{self.escape(description)}</div>")
        else:
            return ''
