from django.db.models import signals
from django.test import TestCase

import factory as fc

from simpel.simpel_partners.models import Partner

from . import factories as fcs


class PartnerModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        with fc.django.mute_signals(signals.post_save):
            cls.users = fcs.UserFactory.create_batch(3)
            cls.cs_organization = fcs.OrganizationCustomerFactory(user=cls.users[0])
            cls.cs_personal = fcs.PersonalCustomerFactory(user=cls.users[1])
            cls.partners = Partner.objects.all()

    def tests_partner_name(self):
        self.assertIsNotNone(self.cs_organization.name)
        self.assertIsNotNone(self.cs_organization.name, str(self.cs_organization))

    def tests_create_partners(self):
        self.assertEqual(self.partners.count(), 2)
        self.assertEqual(self.partners.filter(partner_type=Partner.ORGANIZATION).count(), 1)
        self.assertEqual(self.partners.filter(partner_type=Partner.PERSONAL).count(), 1)

    def test_activate_partner(self):
        with fc.django.mute_signals(signals.post_save):
            self.cs_organization.is_active = False
            self.cs_organization.save()
            self.cs_organization.activate()
            self.assertEqual(self.cs_organization.is_active, True)

    def test_deactivate_partner(self):
        with fc.django.mute_signals(signals.post_save):
            self.cs_organization.is_active = True
            self.cs_organization.save()
            self.cs_organization.deactivate()
            self.assertEqual(self.cs_organization.is_active, False)

    def test_paranoid_deleted_partner(self):
        with fc.django.mute_signals(signals.post_save):
            partner = fcs.OrganizationCustomerFactory(user=self.users[2], is_active=True)
            partner.delete(paranoid=True)
            self.assertEqual(partner.deleted, True)
            self.assertEqual(Partner.objects.get_deleted().count(), 1)
            partner.delete(paranoid=False)
            self.assertEqual(self.partners.count(), 2)
            self.assertEqual(Partner.objects.get_deleted().count(), 0)
