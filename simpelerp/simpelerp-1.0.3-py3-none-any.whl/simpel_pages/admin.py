from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from simpel.simpel_pages.forms import SimpelPageForm
from simpel.simpel_pages.models import SimpelPage, SimpelPageGallery


class PageGalleryInline(admin.StackedInline):
    model = SimpelPageGallery
    extra = 0


@admin.register(SimpelPage)
class SimpelPageAdmin(admin.ModelAdmin):
    form = SimpelPageForm
    list_display = ("url", "title")
    list_filter = ("sites", "registration_required")
    search_fields = ("url", "title")
    inlines = [PageGalleryInline]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "url",
                    "title",
                    "thumbnail",
                    "content",
                    "summary",
                    "allow_comments",
                    "registration_required",
                    "sites",
                )
            },
        ),
        (_("SEO Settings"), {"fields": ("template", "seo_title", "seo_description")}),
    )
