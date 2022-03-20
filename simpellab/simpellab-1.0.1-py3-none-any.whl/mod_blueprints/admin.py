from django.contrib import admin
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.urls import path, reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _

from django_atomics.atoms import DropdownItem
from simpel.simpel_admin.base import ModelAdminMixin
from simpel.simpel_core.templatetags.simpelcore_tags import money

from .models import Blueprint, BlueprintBundle


class BlueprintPermissionMixin:
    def has_add_permission(self, request, obj=None):
        return True if obj and obj.cart.user == request.user else False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True if obj and obj.cart.user == request.user else False

    def has_remove_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True if obj and obj.cart.user == request.user else False


class BlueprintBundleInline(BlueprintPermissionMixin, admin.TabularInline):
    model = BlueprintBundle
    extra = 1
    autocomplete_fields = ["product"]


@admin.register(Blueprint)
class BlueprintAdmin(BlueprintPermissionMixin, ModelAdminMixin):
    raw_id_fields = ["product"]
    search_fields = ("name", "product__name")
    inlines = [BlueprintBundleInline]
    readonly_fields = ("user",)
    list_display = ["product", "total", "object_buttons"]

    def total(self, obj):
        return mark_safe("<div class='text-end'>%s<div>" % money(obj.total))

    total.short_description = mark_safe("<div class='text-end'>%s<div>" % _("Total"))

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    def get_object_buttons_childs(self, request, obj):
        childs = super().get_object_buttons_childs(request, obj)
        childs += [
            DropdownItem(
                url=reverse(admin_urlname(self.opts, "add_to_cart"), args=(obj.id,)),
                classes="btn btn-sm btn-primary",
                label=_("Add to Cart"),
            ),
        ]
        return childs

    def changelist_view(self, request, extra_context=None):
        self.request = request
        return super().changelist_view(request, extra_context)

    def get_urls(self):
        super_urls = super().get_urls()
        urls = [
            path(
                "add_to_cart/<int:pk>/",
                admin.site.admin_view(self.add_to_cart_view),
                name="%s_%s_add_to_cart" % (self.opts.app_label, self.opts.model_name),
            ),
        ]
        urls += super_urls
        return urls

    def add_to_cart_view(self, request, pk):
        # item = get_object_or_404(Blueprint, pk=pk)
        # if not item.user == request.user:
        #     messages.error(request, _("You don't have permission to update or delete this item."))
        #     return redirect(reverse(admin_urlname(Blueprint._meta, "changelist")))
        # cart = Cart.get_for_user(request.user)
        # blueprint = blueprint_to_cart(request, cart, item)
        # messages.success(request, _("%s.") % blueprint)
        # return redirect(reverse(admin_urlname(CartItem._meta, "changelist")))
        return
