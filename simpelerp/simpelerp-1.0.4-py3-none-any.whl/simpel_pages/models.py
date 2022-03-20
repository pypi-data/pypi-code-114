from ckeditor.fields import RichTextField
from django.contrib.sites.models import Site
from django.db import models
from django.urls import NoReverseMatch, get_script_prefix, reverse
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from simpel.simpel_core.models import ModelTemplate


class SimpelPage(models.Model):
    url = models.CharField(_("URL"), max_length=100, db_index=True)
    title = models.CharField(_("title"), max_length=200)
    thumbnail = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="simpelpages",
    )
    content = RichTextField(_("content"), null=True, blank=True)
    seo_title = models.CharField(_("SEO title"), null=True, blank=True, max_length=200)
    seo_description = models.TextField(_("SEO description"), null=True, blank=True)
    summary = RichTextField(_("summary"), null=True, blank=True)
    template = models.ForeignKey(
        ModelTemplate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Template"),
    )
    allow_comments = models.BooleanField(_("allow comments"), default=False)
    registration_required = models.BooleanField(
        _("registration required"),
        help_text=_("If this is checked, only logged-in users will be able to view the page."),
        default=False,
    )
    sites = models.ManyToManyField(Site, verbose_name=_("sites"))

    class Meta:
        verbose_name = _("page")
        verbose_name_plural = _("pages")
        ordering = ["url"]

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        from .views import simpelpage

        for url in (self.url.lstrip("/"), self.url):
            try:
                return reverse(simpelpage, kwargs={"url": url})
            except NoReverseMatch:
                pass
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip("/") + self.url)


class SimpelPageGallery(models.Model):
    page = models.ForeignKey(
        SimpelPage,
        on_delete=models.CASCADE,
        related_query_name="galleries",
        verbose_name=_("page"),
    )
    caption = models.CharField(
        max_length=200,
        verbose_name=_("Caption"),
    )
    thumb_height = models.IntegerField(
        default=100,
        verbose_name=_("Thumbnail Height"),
    )
    thumb_width = models.IntegerField(
        default=100,
        verbose_name=_("Thumbnail Width"),
    )
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="simpelpages_gallery_items",
    )

    class Meta:
        verbose_name = _("Image Gallery")
        verbose_name_plural = _("Image Galleries")
        index_together = ("page", "image")
        ordering = ["page"]
