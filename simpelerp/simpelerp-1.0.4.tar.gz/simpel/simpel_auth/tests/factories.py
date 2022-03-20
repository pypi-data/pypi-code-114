from django.contrib.auth import get_user_model
from django.utils import timezone

import factory as fc
from PIL import Image

from ..models import Profile


def get_temporary_avatar(temp_file):
    size = (200, 200)
    color = (255, 0, 0)
    image = Image.new("RGB", size, color)
    image.save(temp_file, "jpeg")
    return temp_file


class UserFactory(fc.django.DjangoModelFactory):

    first_name = fc.Faker("first_name")
    last_name = fc.Faker("last_name")
    username = fc.Sequence(lambda n: "demouser{}".format(n))
    password = fc.PostGenerationMethodCall("set_password", "dem0user")
    email = fc.LazyAttribute(lambda a: "{}.{}@example.com".format(a.first_name, a.last_name).lower())
    date_joined = fc.LazyFunction(timezone.now)

    class Meta:
        model = get_user_model()
        django_get_or_create = ("username",)


class ProfileFactory(fc.django.DjangoModelFactory):
    user = fc.SubFactory(UserFactory)

    class Meta:
        model = Profile
        django_get_or_create = ("user",)
