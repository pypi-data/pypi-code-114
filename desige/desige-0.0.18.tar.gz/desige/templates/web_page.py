'''
Web page template.

:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

import json

from clabate import Markup, TagAttr

class WebPageTemplate:
    '''
    Based on HTMLPageTemplate
    '''

    html_head = Markup('''
        {head_title}
        {stylesheet}
        {alternate_langs}
        {structured_data}
        {opengraph_data}
        {twitter_data}
        {head_scripts}
        {head_extra}
    ''')

    head_scripts = ''
    head_extra = ''

    @property
    def head_title(self, context):
        title = context['metadata']['title']
        if title:
            return Markup(f"<title>{self.escape(title)} | {context['site_name']}</title>")
        else:
            return Markup(f"<title>{context['site_name']}</title>")

    author = '{metadata[author]}'

    @property
    def alternate_langs(self, context=None):
        return Markup('\n'.join((
            f'<link rel="alternate" hreflang="{self.escape(alt.lang)}" href="{self.escape(alt.url)}"/>'
            for alt in context['layout'].alternate
        )))

    @property
    def structured_data(self, context):
        if 'schema' in context['metadata']:
            schema = json.dumps(context['metadata']['schema'], sort_keys=True, ensure_ascii=False)
            return Markup(f'<script type="application/ld+json">{self.escape(schema)}</script>')
        else:
            return ''

    # XXX article type only, check if subfields are okay for other types
    opengraph_data = Markup('''
        <meta property="og:title" content={escape:attr("""{og_title}""")} />
        <meta property="og:type" content="{og_type}" />
        <meta property="og:type:{og_type}:published_time" content="{metadata[date_created]:%Y-%m-%d}" />
        <meta property="og:type:{og_type}:modified_time" content="{metadata[date_modified]:%Y-%m-%d}" />
        <meta property="og:type:{og_type}:author" content={escape:attr("""{author}""")} />
        <meta property="og:locale:" content="{layout.locale}" />
        <meta property="og:url" content="{layout.url}" />
        <meta property="og:description" content={escape:attr("""{og_description}""")} />
        {og_images}
    ''')

    @property
    def og_title(self, context):
        return context['metadata']['title']

    @property
    def og_description(self, context):
        return context['metadata']['description']

    @property
    def og_type(self, context):
        return 'article'

    @property
    def og_images(self, context):
        images = []
        if 'og_images' in context:
            for url, description in context['og_images']:
                images.append(f'''
                    <meta property="og:image" content="{TagAttr(url)}" />
                    <meta property="og:image:alt" content={TagAttr(description)} />
                ''')
        return Markup('\n'.join(images))

    twitter_data = Markup('''
        <meta property="twitter:card" content="summary_large_image" />
        <meta property="twitter:site" content={escape:attr("""{twitter_site}""")} />
        <meta property="twitter:creator" content={escape:attr("""{twitter_creator}""")} />
        <meta property="twitter:title" content={escape:attr("""{og_title}""")} />
        <meta property="twitter:description" content={escape:attr("""{og_description}""")} />
        {twitter_images}
    ''')

    @property
    def twitter_site(self, context):
        if 'twitter_site' in context['metadata']:
            return context['metadata']['twitter_site']
        elif 'twitter_creator' in context['metadata']:
            return context['metadata']['twitter_creator']
        else:
            return ''

    @property
    def twitter_creator(self, context):
        if 'twitter_creator' in context['metadata']:
            return context['metadata']['twitter_creator']
        else:
            return ''

    @property
    def twitter_images(self, context):
        images = []
        if 'twitter_images' in context:
            for url, description in context['twitter_images']:
                images.append(f'''
                    <meta property="twitter:image" content="{TagAttr(url)}" />
                    <meta property="twitter:image:alt" content={TagAttr(description)} />
                ''')
        return Markup('\n'.join(images))


    @property
    def sitemap_entry(self, context):
        '''
        Sitemap entry should be rendered once, for canonical URL only.
        Canonical URL is for default language.
        Use property instead of attribute for lazy evaluation.
        '''
        lastmod = context['metadata']['date_modified'].strftime('%Y-%m-%d')
        return Markup(f'''
            <url>
                <loc>{context['layout'].url}</loc>
                <lastmod>{lastmod}</lastmod>
                {context['sitemap_alternate_langs']}
                {context['changefreq']}
            </url>
        ''')

    @property
    def sitemap_alternate_langs(self, context):
        return Markup('\n'.join((
            f'<xhtml:link rel="alternate" hreflang="{TagAttr(alt.lang)}" href="{TagAttr(alt.url)}"/>'
            for alt in context['layout'].alternate
        )))

    @property
    def changefreq(self, context):
        if 'changefreq' in context['metadata']:
            return Markup(f"<changefreq>{self.escape(str(context['metadata']['changefreq']))}</changefreq>")
        else:
            return ''
