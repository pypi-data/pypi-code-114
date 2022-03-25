from django import template

register = template.Library()


@register.simple_tag(name="dir", takes_context=True)   # noqa: C901 too complex
def menu_objects(context, object, debug=False):
    object_context = dir(object)
    print(object_context)
    if debug:
        import pdb
        pdb.set_trace()
    return object_context
