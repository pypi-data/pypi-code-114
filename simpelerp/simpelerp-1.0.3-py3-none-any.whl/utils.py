import re
import uuid
from importlib import import_module

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template.defaultfilters import slugify
from django.urls import URLPattern, URLResolver, include
from django.utils.functional import cached_property, lazy
from django.utils.module_loading import module_has_submodule

try:
    from django_hosts.resolvers import reverse as _reverse

    HOSTS_ACTIVE = True
except Exception:
    from django.urls import reverse as _reverse

HOSTS_ACTIVE = getattr(settings, "HOSTS_ACTIVE", False) and HOSTS_ACTIVE


def reverse(
    viewname,
    urlconf=None,
    args=None,
    kwargs=None,
    current_app=None,
    prefix=None,
    host=None,
    host_args=None,
    host_kwargs=None,
    scheme=None,
    port=None,
):
    if HOSTS_ACTIVE:
        return _reverse(
            viewname,
            args=args,
            kwargs=kwargs,
            prefix=prefix,
            current_app=current_app,
            host=host,
            host_args=host_args,
            host_kwargs=host_kwargs,
            scheme=scheme,
            port=port,
        )
    else:
        return _reverse(
            viewname,
            urlconf=urlconf,
            args=args,
            kwargs=kwargs,
            current_app=current_app,
        )


reverse_lazy = lazy(reverse, str)


def get_uid():
    return str(uuid.uuid4())[:8]


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


class DecoratedPatterns(object):
    """
    A wrapper for an urlconf that applies a decorator to all its views.
    """

    def __init__(self, urlconf_module, decorators):
        # ``urlconf_module`` may be:
        #   - an object with an ``urlpatterns`` attribute
        #   - an ``urlpatterns`` itself
        #   - the dotted Python path to a module with an ``urlpatters`` attribute
        self.urlconf = urlconf_module
        try:
            iter(decorators)
        except TypeError:
            decorators = [decorators]
        self.decorators = decorators

    def decorate_pattern(self, pattern):
        if isinstance(pattern, URLResolver):
            decorated = URLResolver(
                pattern.pattern,
                DecoratedPatterns(pattern.urlconf_module, self.decorators),
                pattern.default_kwargs,
                pattern.app_name,
                pattern.namespace,
            )
        else:
            callback = pattern.callback
            for decorator in reversed(self.decorators):
                callback = decorator(callback)
            decorated = URLPattern(
                pattern.pattern,
                callback,
                pattern.default_args,
                pattern.name,
            )
        return decorated

    @cached_property
    def urlpatterns(self):
        # urlconf_module might be a valid set of patterns, so we default to it.
        patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
        return [self.decorate_pattern(pattern) for pattern in patterns]

    @cached_property
    def urlconf_module(self):
        if isinstance(self.urlconf, str):
            return import_module(self.urlconf)
        else:
            return self.urlconf

    @cached_property
    def app_name(self):
        return getattr(self.urlconf_module, "app_name", None)


def decorator_include(decorators, arg, namespace=None):
    """
    A replacement for ``django.conf.urls.include`` that takes a decorator,
    or an iterable of view decorators as the first argument and applies them, in
    reverse order, to all views in the included urlconf.

    from django.contrib import admin
    from django.core.exceptions import PermissionDenied
    from django.urls import path
    from django.contrib.auth.decorators import login_required, user_passes_test

    from decorator_include import decorator_include

    from mysite.views import index

    def only_user(username):
        def check(user):
            if user.is_authenticated and user.username == username:
                return True
            raise PermissionDenied
        return user_passes_test(check)

    urlpatterns = [
        path('', views.index, name='index'),
        # will redirect to login page if not authenticated
        path('secret/', decorator_include(login_required, 'mysite.secret.urls')),
        # will redirect to login page if not authenticated
        # will return a 403 http error if the user does not have the "god" username
        path('admin/', decorator_include([login_required, only_user('god')], admin.site.urls),
    ]

    """
    if isinstance(arg, tuple) and len(arg) == 3 and not isinstance(arg[0], str):
        # Special case where the function is used for something like `admin.site.urls`, which
        # returns a tuple with the object containing the urls, the app name, and the namespace
        # `include` does not support this pattern (you pass directly `admin.site.urls`, without
        # using `include`) but we have to
        urlconf_module, app_name, namespace = arg
    else:
        urlconf_module, app_name, namespace = include(arg, namespace=namespace)
    return DecoratedPatterns(urlconf_module, decorators), app_name, namespace


def extract_contenttype(contenttype_format):
    contenttype_id, app_name, model_name = contenttype_format.split(".")
    result = dict()
    result["model_name"] = model_name
    result["contenttype_model"] = apps.get_model(app_name, model_name)
    result["contenttype_slug"] = ".".join([app_name, model_name])
    result["contenttype_id"] = contenttype_id
    result["app_name"] = app_name
    return result


def get_polymorpohic_choice(models, key_name=None, separator=None, sort_value=False):
    def format_key(ct, sep):
        """return id.app_lable.model_name"""
        if not sep:
            sep = "__"
        if key_name in [None, "id"]:
            return getattr(ct, "id")
        elif len(key_name) == 1:
            return getattr(ct, key_name)
        else:
            return sep.join([str(getattr(ct, field)) for field in key_name])

    contenttype = apps.get_model("contenttypes", "ContentType")
    ct_map = contenttype.objects.get_for_models(*models)
    ct_list = [(format_key(ct, separator), model._meta.verbose_name.title()) for model, ct in ct_map.items()]
    if sort_value:
        sorted(ct_list, key=lambda x: x[1])
    else:
        return ct_list


def get_app_modules():
    """
    Generator function that yields a module object for each installed app
    yields tuples of (app_name, module)
    """
    for app in apps.get_app_configs():
        yield app.name, app.module


def get_app_submodules(submodule_name):
    """
    Searches each app module for the specified submodule
    yields tuples of (app_name, module)
    """
    for name, module in get_app_modules():
        if module_has_submodule(module, submodule_name):
            yield name, import_module("%s.%s" % (name, submodule_name))


def number_to_text_id(number):
    """
    Convert number to sentence (id)
    :param number: interger
    :return: string
    """
    words = [
        "",
        "satu",
        "dua",
        "tiga",
        "empat",
        "lima",
        "enam",
        "tujuh",
        "delapan",
        "sembilan",
        "sepuluh",
        "sebelas",
    ]
    if number < 0:
        number = 0
    number = int(number)
    if number == 0:
        return ""
    elif number < 12 and number != 0:
        return "" + words[number]
    elif number < 20:
        return number_to_text_id(number - 10) + " belas "
    elif number < 100:
        return number_to_text_id(number / 10) + " puluh " + number_to_text_id(number % 10)
    elif number < 200:
        return "seratus " + number_to_text_id(number - 100)
    elif number < 1000:
        return number_to_text_id(number / 100) + " ratus " + number_to_text_id(number % 100)
    elif number < 2000:
        return "seribu " + number_to_text_id(number - 1000)
    elif number < 1000000:
        return number_to_text_id(number / 1000) + " ribu " + number_to_text_id(number % 1000)
    elif number < 1000000000:
        return number_to_text_id(number / 1000000) + " juta " + number_to_text_id(number % 1000000)
    elif number < 1000000000000:
        return number_to_text_id(number / 1000000000) + " milyar " + number_to_text_id(number % 1000000000)
    elif number < 100000000000000:
        return number_to_text_id(number / 1000000000000) + " trilyun " + number_to_text_id(number % 1000000000000)
    elif number <= 100000000000000:
        return "Jumlah terlalu besar!"


def unique_slugify(instance, value, slug_field_name="slug", queryset=None, slug_separator="-"):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = "%s%s" % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[: slug_len - len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = "%s%s" % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator="-"):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ""
    if separator == "-" or not separator:
        re_sep = "-"
    else:
        re_sep = "(?:-|%s)" % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub("%s+" % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != "-":
            re_sep = re.escape(separator)
        value = re.sub(r"^%s+|%s+$" % (re_sep, re_sep), "", value)
    return value
