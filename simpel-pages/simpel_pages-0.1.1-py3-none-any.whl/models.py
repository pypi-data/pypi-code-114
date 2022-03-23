from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import NoReverseMatch, get_script_prefix, reverse
from django.utils.encoding import iri_to_uri
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField
from filer.fields.image import FilerImageField
from mptt.models import MPTTModel, TreeForeignKey
from simpel_themes.models import ModelTemplate
from taggit.managers import TaggableManager
from taggit.models import TagBase, TaggedItemBase

from .utils import unique_slugify


class Category(MPTTModel):

    parent = TreeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="children",
        help_text=_(
            "Categories, unlike tags, can have a hierarchy. You might have a "
            "Jazz category, and under that have children categories for Bebop"
            " and Big Band. Totally optional."
        ),
    )
    name = models.CharField(
        max_length=80,
        unique=True,
        verbose_name=_("Category Name"),
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
        max_length=80,
    )

    icon = "tag-outline"

    class Meta:
        ordering = ["name"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        permissions = (
            ("import_category", _("Can import Category")),
            ("export_category", _("Can export Category")),
        )

    def __str__(self):
        return self.name

    @property
    def opts(self):
        return self.__class__._meta

    def clean(self):
        if self.parent:
            parent = self.parent
            if self.parent == self:
                raise ValidationError("Parent category cannot be self.")
            if parent.parent and parent.parent == self:
                raise ValidationError("Cannot have circular Parents.")

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        return super().save(*args, **kwargs)


class Tag(TagBase):

    icon = "tag-outline"

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    @property
    def opts(self):
        return self._meta


class Page(models.Model):
    url = models.CharField(_("URL"), max_length=100, db_index=True)
    title = models.CharField(_("title"), max_length=200)
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
        max_length=255,
    )
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
    category = models.ForeignKey(
        Category,
        related_name="pages",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Category"),
    )
    tags = TaggableManager(
        through="TaggedPage",
        blank=True,
        related_name="pages",
        verbose_name=_("Tags"),
    )
    allow_comments = models.BooleanField(_("allow comments"), default=False)
    registration_required = models.BooleanField(
        _("registration required"),
        help_text=_("If this is checked, only logged-in users will be able to view the page."),
        default=False,
    )
    sites = models.ManyToManyField(Site, verbose_name=_("sites"), related_name="simpelpages")

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

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.title)
        return super().save(*args, **kwargs)


class TaggedPage(TaggedItemBase):

    content_object = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        related_name="tagged_pages",
        db_index=True,
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tagged_pages",
        db_index=True,
    )

    class Meta:
        verbose_name = _("Tagged Page")
        verbose_name_plural = _("Tagged Pages")

    def __str__(self):
        return str(self.tag)


class PageGallery(models.Model):
    page = models.ForeignKey(
        Page,
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
