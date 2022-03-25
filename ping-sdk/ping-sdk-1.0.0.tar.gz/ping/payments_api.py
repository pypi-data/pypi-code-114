from ping.api_resources.payments_api import merchants
from ping.api_resources.payments_api import paymentOrders
from ping.api_resources.payments_api import payments
from ping.helper.apiHelper import get_base_url


class PaymentsApi:
    """A controller to access all endpoints in the API."""
    def __init__(self, tenant_id="", environment="sandbox"):
        self.tenant_id = tenant_id
        self.environment = environment
        self.base_url = get_base_url(environment)
        self.headers = {
            "Accept": "application/json",
            "tenant_id": tenant_id
            }

    @property
    def merchant(self):
        return Merchant(self.headers, self.base_url)

    @property
    def paymentOrder(self):
        return PaymentOrder(self.headers, self.base_url)

    @property
    def payment(self):
        return Payment(self.headers, self.base_url)


class BaseEndpoints:
    """Endpoint classes inherit from this base class"""
    def __init__(self, headers, base_url):
        self.headers = headers
        self.base_url = base_url


class Merchant(BaseEndpoints):
    """Endpoint class for merchant endpoints"""
    def get_merchants(self):
        return merchants.get_merchants(self.headers, self.base_url)

    def create_new_merchant(self, obj):
        return merchants.create_new_merchant(self.headers, self.base_url, obj)

    def get_specific_merchant(self, merchant_id):
        return merchants.get_specific_merchant(self.headers, self.base_url, merchant_id)


class PaymentOrder(BaseEndpoints):
    """Endpoint class for payment order endpoints"""
    def get_payment_orders(self, date_from=None, date_to=None):
        return paymentOrders.get_payment_orders(self.headers, self.base_url, date_from, date_to)

    def create_payment_order(self, split_tree_id):
        return paymentOrders.create_payment_order(self.headers, self.base_url, split_tree_id)

    def get_payment_order(self, payment_order_id):
        return paymentOrders.get_payment_order(self.headers, self.base_url, payment_order_id)

    def update_payment_order(self, payment_order_id, split_tree_id):
        return paymentOrders.update_payment_order(self.headers, self.base_url, payment_order_id, split_tree_id)

    def close_payment_order(self, payment_order_id):
        return paymentOrders.close_payment_order(self.headers, self.base_url, payment_order_id)

    def settle_payment_order(self, payment_order_id):
        return paymentOrders.settle_payment_order(self.headers, self.base_url, payment_order_id)

    def split_payment_order(self, payment_order_id):
        return paymentOrders.split_payment_order(self.headers, self.base_url, payment_order_id)


class Payment(BaseEndpoints):
    """Endpoint class for payment endpoints"""
    def initiate_payment(self, obj, payment_order_id):
        return payments.initiate_payment(self.headers, self.base_url, obj, payment_order_id)

    def get_payment(self, payment_order_id, payment_id):
        return payments.get_payment(self.headers, self.base_url, payment_order_id, payment_id)
