from django.apps import apps
from django.db import models
from django.template import Library

from ..helpers import URLHelper

register = Library()

_url_helper_registry = {}


@register.simple_tag(takes_context=True)
def object_url(context, namespace, instance, **kwargs):
    if isinstance(instance, models.Model):
        model = instance.__class__
    elif isinstance(instance, str):
        model = apps.get_model(instance)
    else:
        model = instance
    opts = model._meta
    slug = "%s_%s" % (opts.app_label, opts.model_name)
    helper = _url_helper_registry.get(slug, None)
    if not helper:
        helper = URLHelper(namespace, model)
        _url_helper_registry[slug] = helper
    return helper.get_url(**kwargs)


@register.simple_tag(takes_context=True)
def get_opts(context, instance):
    if not isinstance(instance, (models.Model,)):
        raise ValueError("'%s' is not model instance" % instance)
    return instance._meta


@register.filter
def dashboard_urlname(value, arg):
    if isinstance(value, (models.Model,)):
        value = value._meta
    return "dashboard_%s_%s_%s" % (value.app_label, value.model_name, arg)


@register.filter
def website_urlname(value, arg):
    if isinstance(value, (models.Model,)):
        value = value._meta
    return "website_%s_%s_%s" % (value.app_label, value.model_name, arg)
