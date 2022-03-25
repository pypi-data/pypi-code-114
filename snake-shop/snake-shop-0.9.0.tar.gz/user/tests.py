"""Login views unit test"""

# Django
from django.test import TestCase, Client
from django.urls import reverse
# Models
from .models import User


class TestLoginView(TestCase):
    """Test the functionality of the Login view"""
    CREDENTIALS = {
        'username': 'john123',
        'password': '12345',
        # 'password_confirmation': '12345',
        'first_name': 'john',
        'last_name': 'smith',
        'email': 'john@smith.io'
    }

    def setUp(self):
        """Initialise variables."""
        self.user = User.objects.create(**self.CREDENTIALS)
        self.client = Client()
        self.url = reverse('users:login')

    def te111st_basic_login_username(self):
        """Test basic login username"""
        credentials = self.credentials
        import pdb; pdb.set_trace()  # <---------
        response = self.client.post(reverse('users:signup'), **self.CREDENTIALS)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('users:send_email_verification'))
        self.assertEquals(User.objects.get(username='john123').email, 'john@smith.io')

        response = self.client.post(self.url, {
            'username': 'john123',
            'password': '12345'
        })

        self.assertEquals(response.status_code, 302)
        self.assertIsNone(response.context)
        

    def te111st_basic_login_email(self):
        """Test basic login email"""
        response = self.client.post(reverse('users:signup'), {
            'username': 'john123',
            'password': '12345',
            'password_confirmation': '12345',
            'first_name': 'john',
            'last_name': 'smith',
            'email': 'john@smith.io'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('users:send_email_verification'))
        self.assertEquals(User.objects.get(username='john123').email, 'john@smith.io')

        response = self.client.post(self.url, {
            'username': 'john@smith.io',
            'password': '12345'
        })

        self.assertEquals(response.status_code, 302)
        self.assertIsNone(response.context)
