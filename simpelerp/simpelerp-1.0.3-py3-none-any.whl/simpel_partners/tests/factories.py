import factory as fc
from factory.django import DjangoModelFactory

from simpel.simpel_auth.tests.factories import UserFactory

from ..models import Partner


class PartnerFactory(DjangoModelFactory):

    user = fc.SubFactory(UserFactory)

    class Meta:
        model = Partner
        django_get_or_create = ("user",)


class OrganizationCustomerFactory(PartnerFactory):

    name = "{} {}".format(fc.Faker("company", locale="id"), fc.Faker("company_suffix", locale="id"))
    partner_type = Partner.ORGANIZATION
    is_customer = True


class PersonalCustomerFactory(PartnerFactory):

    name = fc.LazyAttribute(lambda a: "{}".format(a.user.get_full_name()))
    partner_type = Partner.PERSONAL
    is_customer = True
