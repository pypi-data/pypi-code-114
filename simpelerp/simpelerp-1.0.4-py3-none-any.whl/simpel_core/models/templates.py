import os
from pathlib import Path

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.template import TemplateDoesNotExist
from django.template.backends.django import DjangoTemplates
from django.template.loader import get_template
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from polymorphic.models import PolymorphicModel

from simpel.utils import unique_slugify

ROOT = Path(__file__).parent


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
        db_table = "simpel_template_category"
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


class TemplateEnabledModel(models.Model):

    template = None
    backend = DjangoTemplates

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @cached_property
    def engine(self):
        return self.backend(
            {
                "APP_DIRS": True,
                "DIRS": [
                    os.path.join(settings.BASE_DIR, "mediafiles", self.backend.app_dirname),
                    os.path.join(settings.PROJECT_DIR, self.backend.app_dirname),
                    ROOT / self.backend.app_dirname,
                ],
                "NAME": "simpeltemplate",
                "OPTIONS": {},
            }
        )

    def render(self, context, request=None):
        template = self.get_template()
        return mark_safe(template.render(context, request=request).strip())

    def get_template(self):
        if self.template is None:
            raise NotImplementedError("subclasses must provide template or implement get_template()")
        return get_template(self.template)


class ModelTemplate(TemplateEnabledModel, PolymorphicModel):
    thumbnail = models.ImageField(
        verbose_name=_("Thumbnail"),
        null=True,
        blank=True,
    )
    name = models.CharField(
        _("Name"),
        max_length=80,
    )
    category = TreeForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="templates",
        verbose_name=_("Category"),
    )

    icon = "view-dashboard-outline"

    class Meta:
        ordering = ["name"]
        verbose_name = _("Template")
        verbose_name_plural = _("Templates")
        db_table = "simpel_template"

    @cached_property
    def specific(self):
        return self.get_real_instance()

    def __str__(self):
        return self.name


class FileModelTemplate(ModelTemplate):
    template = models.FileField(_("Template File"), upload_to="templates")

    class Meta:
        verbose_name = _("File Template")
        verbose_name_plural = _("File Templates")
        db_table = "simpel_template_file"

    def get_template(self):
        with open(str(self.template.file)) as f:
            contents = f.read()
            return self.engine.from_string(contents)


class PathModelTemplate(ModelTemplate):
    template = models.CharField(
        _("Template Path"),
        max_length=80,
    )

    class Meta:
        verbose_name = _("Path Template")
        verbose_name_plural = _("Path Templates")
        db_table = "simpel_template_path"

    def clean(self):
        try:
            self.get_template()
        except TemplateDoesNotExist as err:
            raise ValidationError({"template": _("%s doesn't exist!") % err})

    def get_template(self):
        return get_template(self.template)


class StringModelTemplate(ModelTemplate):
    template = models.TextField(_("Template String"))

    class Meta:
        verbose_name = _("String Template")
        verbose_name_plural = _("String Templates")
        db_table = "simpel_template_string"

    def get_template(self):
        return self.engine.from_string(self.template)
