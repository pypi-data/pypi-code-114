from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .forms import PageForm
from .models import Category, Page, PageGallery, Post


class PageGalleryInline(admin.StackedInline):
    model = PageGallery
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageForm
    list_display = ("url", "title")
    list_filter = ("sites", "registration_required")
    search_fields = ("url", "title")
    inlines = [PageGalleryInline]
    seo_settings = (_("SEO Settings"), {"fields": ("template", "seo_title", "seo_description")})
    page_fields = ("parent", "url", "title", "category", "tags", "allow_comments", "registration_required", "sites")
    fieldsets = (
        (None, {"fields": page_fields}),
        seo_settings,
    )


@admin.register(Post)
class PostAdmin(PageAdmin):
    inlines = [PageGalleryInline]
    page_fields = (
        "url",
        "title",
        "thumbnail",
        "content",
        "category",
        "tags",
        "summary",
        "allow_comments",
        "registration_required",
        "sites",
    )
    fieldsets = (
        (None, {"fields": page_fields}),
        PageAdmin.seo_settings,
    )
