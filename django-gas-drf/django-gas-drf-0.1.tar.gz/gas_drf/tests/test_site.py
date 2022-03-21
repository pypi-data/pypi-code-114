from django.test import TestCase
from django.urls import reverse

from gas_drf.sites import GASDRFSite


class SiteTestCase(TestCase):
    def test_register(self):
        from gas_drf.gas.users.api_views import UserViewSet
        test_site = GASDRFSite()

        test_site.register('users-test', UserViewSet, basename='gas-user-test')
        registered_url_names = [
            url.name for url in test_site.urls
        ]
        self.assertIn('gas-user-test-list', registered_url_names)


class SampleAppIntegrationTest(TestCase):
    def test_gas_autodiscover(self):
        # urls registered
        reverse('gas-user-list')
