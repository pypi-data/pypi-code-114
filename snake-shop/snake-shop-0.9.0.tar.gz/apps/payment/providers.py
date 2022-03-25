from django.http.request import HttpRequest
from oscar.apps.checkout.utils import CheckoutSessionData
from apps.address import models as address_models
from apps.basket.models import Basket
from .forms import SelectBankAccountForm
from .models import SourceType


class ProviderManager:
    def get_system_providers(self, request):
        assert isinstance(request, HttpRequest)
        return SourceType.objects.filter(
            enabled=True, partners__in=request.partners)

    def get_allowed_for_address(self, request, user_address):
        providers = []
        assert user_address
        for provider in self.get_system_providers(request):
            if provider.allowed_for_user_address(user_address):
                providers.append(provider)
        return providers

    def get_providers_for_checkout(self, request, checkout_session, basket):
        assert isinstance(request, HttpRequest)
        assert isinstance(checkout_session, CheckoutSessionData)
        assert isinstance(basket, Basket)

        address_id = checkout_session.user_address_id()
        address = address_models.UserAddress.objects.get(id=address_id)

        providers = list(self.get_allowed_for_address(request, address))
        for provider in providers:
            provider.is_allowed = provider.allowed_for_checkout(
                checkout_session, basket
            )
            if provider.bankcard_needed:
                provider.form = SelectBankAccountForm(
                    checkout_session.request, address
                )
        return providers
