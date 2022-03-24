# -*- coding: utf-8 -*-

import logging
from plone import api
from redturtle.chefcookie.interfaces import IChefCookieSettings
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides

logger = logging.getLogger(__name__)

DEFAULT_PROFILE = "profile-redturtle.chefcookie:default"


def update_profile(context, profile, run_dependencies=True):
    context.runImportStepFromProfile(DEFAULT_PROFILE, profile, run_dependencies)


def update_registry(context):
    update_profile(context, "plone.app.registry", run_dependencies=False)
    logger.info("Update registry")


def update_to_1002(context):
    alsoProvides(context.REQUEST, IDisableCSRFProtection)
    update_registry(context)
    api.portal.set_registry_record("enable_cc", True, interface=IChefCookieSettings)
