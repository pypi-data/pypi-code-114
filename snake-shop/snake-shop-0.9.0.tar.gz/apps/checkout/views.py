from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.views import generic
from django.contrib import messages
from oscar.apps.checkout import views
from oscar.apps.shipping.methods import NoShippingRequired

from apps.address import forms as address_forms
from apps.address import models as address_models
from apps.payment.providers import ProviderManager
from . import forms, session


class ShippingAddressView(views.ShippingAddressView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['selector_form'] = forms.AddressSelectorForm(
            user=ctx['user'], **self.get_form_kwargs(),
            addresses=self.get_available_addresses(),
        )
        return ctx

    def post(self, request, *args, **kwargs):
        if 'shipping_address' in request.POST:
            addresses = self.get_available_addresses()
            form = forms.AddressSelectorForm(
                request.user, addresses, request.POST)
            if form.is_valid():
                # DB values are set inside form.valid
                shipping_address_pk = int(form.cleaned_data['shipping_address'])
                shipping_address = address_models.UserAddress.objects.get(
                    pk=shipping_address_pk
                )
                self.checkout_session.ship_to_user_address(shipping_address)
                if int(form.cleaned_data['billing_address']) > 0:
                    billing_addr_pk = int(form.cleaned_data['billing_address'])
                    billing_address = address_models.UserAddress.objects.get(
                        pk=billing_addr_pk
                    )
                    self.checkout_session.bill_to_user_address(billing_address)
                else:
                    self.checkout_session.bill_to_user_address(shipping_address)
                return redirect(self.get_success_url())
        return views.ShippingAddressView.post(self, request, *args, **kwargs)


class UserAddressUpdateView(session.CheckoutSessionMixin, generic.UpdateView):
    """
    Update a user address
    """
    template_name = 'oscar/checkout/user_address_form.html'
    form_class = address_forms.UserAddressForm
    success_url = reverse_lazy('checkout:shipping-address')

    def get_queryset(self):
        return self.request.user.addresses.all()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        messages.info(self.request, _("Address saved"))
        return super().get_success_url()


class ShippingMethodView(views.ShippingMethodView):
    def get_methods_as_forms(self, methods):
        method_forms = []
        for method in methods:
            address_id = self.checkout_session.user_address_id()
            address = address_models.UserAddress.objects.filter(
                id=address_id
            ).first()
            method_form = forms.SingleShippingMethodForm(
                method, self.request, address
            )
            method_forms.append(method_form)
        return method_forms

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method_forms'] = self.get_methods_as_forms(context['methods'])
        return context

    def get(self, request, *args, **kwargs):
        if not request.basket.is_shipping_required():
            self.checkout_session.use_shipping_method(
                NoShippingRequired().code)
            return self.get_success_response()

        if not self.checkout_session.is_shipping_address_set():
            messages.error(request, _("Please choose a shipping address"))
            return redirect('checkout:shipping-address')

        self._methods = self.get_available_shipping_methods()
        method_forms = self.get_context_data()['method_forms']
        if len(self._methods) == 0:
            messages.warning(request, _(
                "Shipping is unavailable for your chosen address - please "
                "choose another"))
            return redirect('checkout:shipping-address')
        elif len(self._methods) == 1 and not method_forms[0].fields:
            method_code = method_forms[0].method.code
            self.checkout_session.use_shipping_method(method_code)
            return redirect('checkout:payment-details')
        # Skip get method of parent view:
        return super(session.CheckoutSessionMixin, self).get(
            request, *args, **kwargs
        )

    def post(self, request, *args, **kwargs):
        methods = self.get_available_shipping_methods()
        self._methods = getattr(self, '_methods', methods)

        method_code = request.POST.get('method_code')
        method = methods.get(code=method_code)

        address_id = self.checkout_session.user_address_id()
        # shipping_addr
        address = address_models.UserAddress.objects.get(id=address_id)

        form = forms.SingleShippingMethodForm(method, self.request, address)
        if form.is_valid():
            if address:
                address.floor_number = form.cleaned_data.get('floor_number')
                address.save()
            self.checkout_session.set_delivery(form.get_result())
        else:
            return self.form_invalid(form)
        self.checkout_session.use_shipping_method(method_code)
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        """ Skip Oscars form_invalid """
        for _, message in form.errors.items():
            messages.error(self.request, message)
        return super(generic.edit.FormView, self).form_invalid(form)


class PaymentMethodView(views.PaymentMethodView):
    skip_conditions = []


class PaymentDetailsView(views.PaymentDetailsView):
    template_name = 'oscar/checkout/payment_details.html'

    def skip_unless_payment_is_required(self, request):
        """
        Avoid skipping when price is hidden
        """
        if not request.user.hide_price:
            super().skip_unless_payment_is_required(request)

    @property
    def providers(self):
        providers = ProviderManager().get_providers_for_checkout(
            self.request, self.checkout_session, self.request.basket
        )
        return providers

    @property
    def all_providers(self):
        return ProviderManager().get_system_providers(self.request)

    def get_provider_by_code(self, code):
        for provider in self.providers:
            if provider.code == code:
                return provider

    def get_context_data(self, **kwargs):
        context = views.PaymentDetailsView.get_context_data(self, **kwargs)
        context['providers'] = self.providers
        context['max_providers'] = self.all_providers.count()

        provider_code = self.checkout_session.payment_method()
        if provider_code:
            selected_provider = self.get_provider_by_code(provider_code)
            context['selected_provider'] = selected_provider
        context['order_note_form'] = forms.OrderNoteForm(self.checkout_session)
        context['is_preview'] = self.preview
        return context

    def get(self, request, *args, **kwargs):
        if 'bankacc' in request.GET:
            bankcard = request.user.bankcards.get(
                id=int(request.GET['bankacc'])
            )
            user_address = request.user.addresses.get(
                id=self.checkout_session.user_address_id()
            )
            user_address.default_bank_account = bankcard
            user_address.save()
        if not self.preview and len(self.providers) == 1 \
                and not self.providers[0].form:
            self.checkout_session.pay_by(self.providers[0].code)
            self.preview = True
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'method_code' in self.request.POST:
            self.checkout_session.pay_by(self.request.POST['method_code'])

        if 'bank_accounts' in self.request.POST:
            bank_account = self.request.POST['bank_accounts']
            self.checkout_session.set_bank_account(bank_account)
            user = self.request.user
            user.default_bank_account = self.bank_account
            user.save()

        self.check_pre_conditions(request)
        return super().post(request, site=request.site, *args, **kwargs)
