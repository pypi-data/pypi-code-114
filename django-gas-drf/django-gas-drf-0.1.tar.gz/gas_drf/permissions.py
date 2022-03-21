from rest_framework.permissions import BasePermission


class HasValidRole(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        roles = set(view.roles)
        roles.add(view.base_role)
        access_denied = (
            not user.is_authenticated or (
                not user.is_superuser
                and not user.user_roles.filter(role__in=roles).exists()
            )
        )
        return not access_denied
