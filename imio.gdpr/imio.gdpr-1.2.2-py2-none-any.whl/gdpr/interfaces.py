# -*- coding: utf-8 -*-
from imio.gdpr import _
from imio.gdpr import get_default_text
from imio.gdpr import get_default_cookies_text
from imio.gdpr import HAS_PLONE_5_AND_MORE
from plone.autoform import directives as form
from plone.supermodel import model
from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IImioGdprLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IGDPRSettings(model.Schema):
    """Schema for the control panel form."""

    if not HAS_PLONE_5_AND_MORE:
        # remove on deprecation of Plone 4.3
        from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

        form.widget("text", WysiwygFieldWidget)
        form.widget("cookies_text", WysiwygFieldWidget)
    else:
        form.widget("text", klass="pat-tinymce")
        form.widget("cookies_text", klass="pat-tinymce")

    text = schema.Text(
        title=_("title_text", default="Body text"),
        description=_("help_text", default="The text of the GDPR explanation."),
        required=True,
        defaultFactory=get_default_text,
    )

    is_text_ready = schema.Bool(
        title=_("is_text_ready_text", default="Is text ready ?"),
        description=_(
            "help_is_text_ready",
            default="Is text is not ready, it should not be visible",
        ),
        required=True,
        default=False,
    )

    cookies_text = schema.Text(
        title=_("title_cookies_text", default="Cookies text"),
        description=_(
            "help_cookies_text", default="The text of the Cookies Policy page."
        ),
        required=True,
        defaultFactory=get_default_cookies_text,
    )
