from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import (Configuration, SocialLink, CompanyMixin, EmailConfigMixin,
                     ColorMixin, ImageMixin)


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 0
    classes = ['collapse']


class ConfigurationAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]
    fieldsets = [
        (None, {'fields': ['site']}),
        (_('Firmeneindaten'), {
            'classes': ('collapse',),
            'fields': [field.name for field in CompanyMixin._meta.get_fields()],
        }),
        (_('Farben'), {
            'classes': ('collapse',),
            'fields': [field.name for field in ColorMixin._meta.get_fields()],
        }),
        (_('Bilder'), {
            'classes': ('collapse',),
            'fields': [field.name for field in ImageMixin._meta.get_fields()],
        }),
        (_('Email'), {
            'classes': ('collapse',),
            'fields': [field.name for field in EmailConfigMixin._meta.get_fields()],
        }),
        (_('Sonstiges'), {
            'classes': ('collapse',),
            'fields': ['home_bottom_text', 'google_site_id',
                       'basket_sumup_with_deposit', 'show_all_products'],
        }),
    ]


admin.site.register(Configuration, ConfigurationAdmin)
