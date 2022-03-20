import os
import tempfile
import uuid

from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from simpel.simpel_auth.models import Profile, upload_avatar_to

from . import factories as fcs


class ProfileModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.users = fcs.UserFactory.create_batch(3)
        cls.profiles = fcs.ProfileFactory.create_batch(3)
        cls.user = cls.users[0]

    def setUp(self):
        return super().setUp()

    def test_create_profile_with_signal(self):
        """Test creating user will create profile automatically"""
        users_count = get_user_model().objects.count()
        profile_counts = Profile.objects.count()

        # with 2 users from init admin

        self.assertEqual(profile_counts, 6)
        self.assertEqual(users_count, 6)

    def test_preferred_language(self):
        lang = self.user.profile.get_preferred_language()
        self.assertIsNotNone(lang)

    def test_preferred_timezone(self):
        tz = self.user.profile.get_current_time_zone()
        self.assertIsNotNone(tz)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_avatar_upload_to(self):
        filename = "example_img.png"
        uid = uuid.uuid4()
        test_path = os.path.join(
            "avatar_images",
            "avatar_{uuid}_{filename}".format(uuid=uid, filename=filename),
        )
        avatar_path = upload_avatar_to(None, filename, uid=uid)
        self.assertEqual(test_path, avatar_path)
