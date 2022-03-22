from functools import wraps


def maintenance(test_func):
    """
    Decorator for views that checks whether a site is in maintenance mode.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            from simpel_routers.views import MaintenanceView

            if not test_func(request.user):
                return view_func(request, *args, **kwargs)
            else:
                return MaintenanceView.as_view()(request, *args, **kwargs)

        return _wrapped_view

    return decorator


def maintainer_required(function=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = maintenance(lambda u: not u.is_superuser)
    if function:
        return actual_decorator(function)
    return actual_decorator
