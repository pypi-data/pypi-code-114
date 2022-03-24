from django.utils.functional import lazy

try:
    from django_hosts.resolvers import reverse as _reverse

    HOSTS_ACTIVE = True
except Exception:
    from django.urls import reverse as _reverse

    HOSTS_ACTIVE = False


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
