import base64

from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework import HTTP_HEADER_ENCODING, status, serializers
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.test import APIRequestFactory

from gas_drf.permissions import HasValidRole

factory = APIRequestFactory()


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SampleView(ListAPIView):
    permission_classes = [HasValidRole]
    authentication_classes = [BasicAuthentication]
    base_role = 'admins'
    roles = ('test_admins',)
    queryset = User.objects.all()
    serializer_class = SampleSerializer


sample_view = SampleView.as_view()


def basic_auth_header(username, password):
    credentials = ('%s:%s' % (username, password))
    base64_credentials = base64.b64encode(credentials.encode(HTTP_HEADER_ENCODING)).decode(HTTP_HEADER_ENCODING)
    return 'Basic %s' % base64_credentials


class PermissionTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('disallowed', 'disallowed@example.com', 'password')
        user = User.objects.create_user('permitted', 'permitted@example.com', 'password')
        user.user_roles.create(
            role='admins'
        )
        user = User.objects.create_user('permitted2', 'permitted2@example.com', 'password')
        user.user_roles.create(
            role='test_admins'
        )

        self.admins_credentials = basic_auth_header('permitted', 'password')
        self.other_admin_credentials = basic_auth_header('permitted2', 'password')
        self.disallowed_credentials = basic_auth_header('disallowed', 'password')

    def test_has_valid_role(self):
        # Users without roles can't access
        request = factory.get(
            '/', format='json',
            HTTP_AUTHORIZATION=self.disallowed_credentials)
        response = sample_view(request)
        self.assertEqual(
            response.status_code, status.HTTP_403_FORBIDDEN)

        # Users with the 'admins' role can access
        request = factory.get(
            '/', format='json',
            HTTP_AUTHORIZATION=self.admins_credentials)
        response = sample_view(request)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)

        # Users with the 'test_admins' role can access
        request = factory.get(
            '/', format='json',
            HTTP_AUTHORIZATION=self.other_admin_credentials)
        response = sample_view(request)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
