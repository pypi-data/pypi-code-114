from functools import reduce

from rest_framework.exceptions import PermissionDenied


def authorize(*permissions):
    permissions = [permission() for permission in permissions]

    def decorator(func):
        def wrap(*args, **kwargs):
            self = args[0]
            request = args[1]
            obj = self.kwargs.get("obj")
            booleans = map(
                lambda permission: permission.has_permission(
                    request,
                    self
                ) and permission.has_object_permission(
                    request,
                    self,
                    obj
                ),
                permissions
            )
            is_permitted = reduce(lambda val, boolean: val or boolean, booleans)
            if not is_permitted:
                raise PermissionDenied
            return func(*args, **kwargs)
        return wrap
    return decorator
