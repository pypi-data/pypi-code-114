from django.contrib import admin, messages
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import path, reverse
from django.utils.translation import gettext as _

from simpel.simpel_admin.base import AdminFormView
from simpel.simpel_auth.models import Activity
from simpel.simpel_partners.models import Partner
from simpel.simpel_sales.helpers import create_salesorder, create_salesquotation
from simpel.simpel_sales.models import SalesOrder, SalesQuotation
from simpel.simpel_shop.admin import ShopAdmin as BaseShopAdmin
from simpel.simpel_shop.models import Cart, CartItem

from .forms import CheckoutForm


class AdminCheckoutView(AdminFormView):
    template_name = "admin/simpel_shop/custom_checkout.html"
    model_admin = None
    shop_adapter = None

    def __init__(self, model_admin, **kwargs):
        self.model_admin = model_admin
        self.shop_adapter = model_admin.shop_adapter
        super().__init__(**kwargs)

    def has_permission(self, request=None):
        if not self.model_admin.has_add_permission(request):
            return False
        # if not hasattr(self.request.user, "partner"):
        #     return False
        so_perm = request.user.has_perm("simpel_sales.add_salesorder")
        sq_perm = request.user.has_perm("simpel_sales.add_salesquotation")
        if request.method == "POST":
            if self.action == "create_salesorder":
                return so_perm
            elif self.action == "create_salesquotation":
                return sq_perm
            else:
                return False
        elif request.method == "GET":
            return so_perm or sq_perm
        else:
            return False

    def dispatch(self, request, *args, **kwargs):
        self.cart = Cart.get_for_user(self.request.user)
        self.action = request.POST.get("_checkout_action")
        if not self.has_permission(request):
            messages.error(request, _("You don't have any permission!"))
            return redirect(reverse(admin_urlname(CartItem._meta, "changelist")))
        if not self.cart.items.count():
            messages.error(request, _("Your cart is empty, please add a product or service!"))
            return redirect(reverse(admin_urlname(CartItem._meta, "changelist")))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.action == "create_salesorder":
            messages.success(self.request, _("Sales Order created, complete payment and send confirmation."))
            return reverse(admin_urlname(SalesOrder._meta, "inspect"), args=(self.instance.id,))
        elif self.action == "create_salesquotation":
            messages.success(self.request, _("Sales Quotation created."))
            return reverse(admin_urlname(SalesQuotation._meta, "inspect"), args=(self.instance.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": _("Create Order"),
                "opts": CartItem._meta,
                "cart": self.cart,
                "cancel_url": reverse(admin_urlname(CartItem._meta, "changelist")),
                "add": False,
                "change": False,
            }
        )
        return context

    def get_form_class(self):
        return CheckoutForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs

    def get_checkout_handler(self, action):
        action_map = {
            "create_salesorder": create_salesorder,
            "create_salesquotation": create_salesquotation,
        }
        return action_map[action]

    def log_creation(self):
        Activity.objects.log_action(
            self.request.user,
            self.instance,
            Activity.CREATION,
            note="Create %s" % self.instance,
        )

    def form_valid(self, form):
        data = form.cleaned_data
        data["data"] = {
            "sampling_options": data.pop("sampling_options"),
            "sampling_schedule": data.pop("sampling_schedule").strftime("%d-%m-%Y"),
            "sampling_estimation": data.pop("sampling_estimation"),
        }
        billing_address = data.pop("billing_address")
        shipping_address = data.pop("shipping_address")
        items = self.shop_adapter.get_filtered_items(data["group"].code)
        handler = self.get_checkout_handler(self.action)
        self.instance = handler(
            self.request,
            data=data,
            items=items,
            billing=billing_address,
            shipping=shipping_address,
            delete_item=True,
            from_cart=True,
        )
        self.log_creation()
        return redirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        if self.action not in self.shop_adapter.valid_action:
            messages.error(request, _("Invalid checkout action!"))
            return redirect(self.model_admin.get_changelist_url())
        return super().post(request, *args, **kwargs)


class ShopAdmin(BaseShopAdmin):
    checkout_view_class = AdminCheckoutView

    def get_checkout_form(self):
        """Return an instance of the form to be used in this view."""
        form_class = CheckoutForm
        kwargs = {"request": self.request}
        if self.request.method in ("POST", "PUT"):
            kwargs.update({"data": self.request.POS, "files": self.request.FILES})
        return form_class(**kwargs)

    def get_urls(self):
        super_urls = super().get_urls()
        urls = [
            path(
                "hx-customer-address/",
                admin.site.admin_view(self.htmx_customer_address),
                name="%s_%s_hx_customer_address" % (self.opts.app_label, self.opts.model_name),
            ),
        ]
        urls += super_urls
        return urls

    def htmx_customer_address(self, request):
        from .forms import CheckoutAddressForm

        if request.htmx:
            customer_id = request.GET["customer"]
            if customer_id not in ["", None]:
                customer = Partner.objects.filter(pk=customer_id).first()
            else:
                customer = None
            form = CheckoutAddressForm(customer=customer)
            return render(request, "admin/simpel_shop/address_form.html", context={"form": form})
        else:
            raise Http404()
