"""snake-shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from collections import OrderedDict
from django.apps import apps
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.urls import path
from django.urls.conf import include
from django.views.static import serve
from django.views.generic.base import TemplateView

from oscar.views import handler403, handler404, handler500
from newsletter.generator.views import MessageGeneratorView
from .sitemaps import base_sitemaps

admin.autodiscover()
sitemaps = OrderedDict()
sitemaps.update({'flatpages': FlatPageSitemap})
sitemaps.update(base_sitemaps)

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain', extra_context={'STAGE': settings.STAGE})),
    path('api/', include("api.urls")),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('dashboard/product_tables/', apps.get_app_config('product_tables_dashboard').urls),
    path('newsletter/', include('newsletter.urls')),
    path('', include(apps.get_app_config('oscar').urls[0])),
    prefix_default_language=settings.URL_PREFIX_DEFAULT_LANGUAGE,
)

if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns

    import debug_toolbar
    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        path('403', handler403, {'exception': Exception()}),
        path('404', handler404, {'exception': Exception()}),
        path('500', handler500),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
