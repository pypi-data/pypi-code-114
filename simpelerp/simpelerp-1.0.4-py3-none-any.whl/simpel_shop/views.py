from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, View

from simpel.simpel_products.models import Product
from simpel.simpel_shop.models import Cart

from .settings import simpel_shop_settings as shop_settings


class AddItemView(View):
    def get_success_url(self):
        raise NotImplementedError(
            _("%s must implement get_success_url()") % self.__class__.__name__,
        )

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        self.shop_adapter = self.get_shop_adapter(request)
        self.shop_adapter.add_item(product)
        messages.success(request, _("%s added to cart."))
        return redirect(self.get_success_url())

    def get_shop_adapter(self, request):
        return self.shop_adapter_class(request)


class AddItemFormView(FormView):
    template_name = "admin/simpel_shop/cart_add_item.html"
    shop_adapter_class = shop_settings.ADAPTER_CLASS
    form_class = shop_settings.SHOP_ADMIN_ADDITEM_FORM

    def get_form_class(self):
        return self.form_class

    def dispatch(self, request, pk, *args, **kwargs):
        self.request = request
        self.product = get_object_or_404(Product, pk=pk)
        self.cart = Cart.get_for_user(request.user)
        self.shop_adapter = self.get_shop_adapter(request)
        return super().dispatch(request, pk, *args, **kwargs)

    def get_success_url(self):
        raise NotImplementedError(
            _("%s must implement get_success_url()") % self.__class__.__name__,
        )

    def get_cancel_url(self):
        raise NotImplementedError(
            _("%s must implement get_cancel_url()") % self.__class__.__name__,
        )

    def get_shop_adapter(self, request):
        return self.shop_adapter_class(request)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.product
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel_url"] = self.get_cancel_url
        context["title"] = _("Add %s") % self.product
        context["product"] = self.product
        context["cart"] = self.cart
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        self.shop_adapter.add_item(self.product, **data)
        return super().form_valid(form)


class SimpleCheckoutView(FormView):
    template_name = "admin/simpel_shop/checkout.html"
    shop_adapter_class = shop_settings.ADAPTER_CLASS

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        if not self.has_permissions():
            messages.error(self.request, _("You don't have any permissions!"))
            return redirect(reverse("admin:simpel_shop_cartitem_changelist"))
        self.shop_adapter = self.get_shop_adapter(request)
        return super().dispatch(request, *args, **kwargs)

    def get_template_names(self):
        return self.template_name

    def get_shop_adapter(self, request):
        return self.shop_adapter_class(request)

    def has_permissions(self):
        return True


def customer_selection_condition(wizzard):
    user = wizzard.request.user
    return user.is_staff or user.is_superadmin
