# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from imio.gdpr import HAS_PLONE_5_AND_MORE
from imio.gdpr.interfaces import IGDPRSettings
from imio.gdpr.interfaces import IImioGdprLayer
from imio.gdpr.testing import IMIO_GDPR_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

if HAS_PLONE_5_AND_MORE:
    from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that imio.gdpr is properly installed."""

    layer = IMIO_GDPR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if not HAS_PLONE_5_AND_MORE:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        else:
            self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if imio.gdpr is installed."""
        if not HAS_PLONE_5_AND_MORE:
            self.assertTrue(self.installer.isProductInstalled("imio.gdpr"))
        else:
            self.assertTrue(self.installer.is_product_installed("imio.gdpr"))

    def test_browserlayer(self):
        """Test that IImioGdprLayer is registered."""
        from plone.browserlayer import utils

        self.assertIn(IImioGdprLayer, utils.registered_layers())

    def test_default_values(self):
        record = api.portal.get_registry_record("text", interface=IGDPRSettings)
        self.assertIn("<h2>D\xe9claration relative", record)

        record = api.portal.get_registry_record("cookies_text", interface=IGDPRSettings)
        self.assertIn("<h1>Politique d'utilisation des cookies", record)


class TestUninstall(unittest.TestCase):

    layer = IMIO_GDPR_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if not HAS_PLONE_5_AND_MORE:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        else:
            self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        if not HAS_PLONE_5_AND_MORE:
            self.installer.uninstallProducts(["imio.gdpr"])
        else:
            self.installer.uninstall_product("imio.gdpr")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if imio.gdpr is cleanly uninstalled."""
        if not HAS_PLONE_5_AND_MORE:
            self.assertFalse(self.installer.isProductInstalled("imio.gdpr"))
        else:
            self.assertFalse(self.installer.is_product_installed("imio.gdpr"))

    def test_browserlayer_removed(self):
        """Test that IImioGdprLayer is removed."""
        from plone.browserlayer import utils

        self.assertNotIn(IImioGdprLayer, utils.registered_layers())
