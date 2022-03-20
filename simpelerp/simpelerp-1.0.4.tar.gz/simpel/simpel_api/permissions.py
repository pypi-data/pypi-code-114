from rest_framework.permissions import BasePermission


class IsPartner(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and hasattr(request.user, "partner"))


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        partner = getattr(request.user, "partner", None)
        customer = False if not partner else partner.is_customer
        return bool(request.user and customer)


class IsSupplier(BasePermission):
    def has_permission(self, request, view):
        partner = getattr(request.user, "partner", None)
        customer = False if not partner else partner.is_supplier
        return bool(request.user and customer)


class IsPartnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user) and bool(hasattr(request.user, "partner") or request.user.is_staff)
