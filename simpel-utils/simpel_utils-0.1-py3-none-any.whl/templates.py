from django.core.exceptions import ImproperlyConfigured


def get_template_name(template_name, theme_name=None):
    if theme_name is not None:
        if isinstance(theme_name, str):
            theme_name = "%s/" % theme_name
            return "%s%s" % (theme_name, template_name)
        else:
            raise ImproperlyConfigured("theme_name must be string")
    else:
        return template_name


def get_template_names(template_names, theme_name=None):
    templates = list()
    for template in template_names:
        template_name = get_template_name(template, theme_name)
        templates.append(template_name)
    return templates
