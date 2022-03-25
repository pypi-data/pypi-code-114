from django.test import TestCase, Client


class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.user = Client()
