# coding: utf-8
from __future__ import absolute_import
from django.conf import settings
from django.conf.urls import url

from creadoc.controller import creadoc_controller

__author__ = 'damirazo <me@damirazo.ru>'


def register_urlpatterns():
    return (
        url('^{}'.format(settings.CREADOC_URL),
            creadoc_controller.process_request),
    )
