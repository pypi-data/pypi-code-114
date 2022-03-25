from django import template


register = template.Library()


@register.simple_tag(name='sidebar_block_collapsed', takes_context=True)
def sidebar_block_collapsed(context, sidebar_code):
    collapsed_sidebars = context.request.session.get('collapsed_sidebars')
    if not sidebar_code:
        return collapsed_sidebars
    if collapsed_sidebars:
        return collapsed_sidebars.get(sidebar_code)
    return False
