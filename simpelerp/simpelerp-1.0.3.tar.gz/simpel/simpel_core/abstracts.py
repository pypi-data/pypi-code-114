from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone, translation
from django.utils.functional import cached_property
from polymorphic.managers import PolymorphicManager

_ = translation.ugettext_lazy


class ParanoidManagerMixin:
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    def get(self, *args, **kwargs):
        kwargs["deleted"] = False
        return super().get(*args, **kwargs)

    def get_deleted(self):
        return super().get_queryset().filter(deleted=True)


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class BasePolymorphicManager(PolymorphicManager):
    pass


class ParanoidPolymorphicManager(ParanoidManagerMixin, PolymorphicManager):
    """Implement paranoid mechanism queryset"""

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    def get(self, *args, **kwargs):
        kwargs["deleted"] = False
        return super().get(*args, **kwargs)

    def get_deleted(self):
        return super().get_queryset().filter(deleted=True)

    def delete(self, paranoid=False):
        return super().delete()


class ParanoidManager(ParanoidManagerMixin, BaseManager):
    pass


class BaseSnippetManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class SnippetManager(BaseSnippetManager):
    pass


# Deprecated
class SimpleBaseModel(models.Model):
    class Meta:
        abstract = True

    modified_at = models.DateTimeField(default=timezone.now, editable=False)

    @cached_property
    def opts(self):
        return self.__class__._meta

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self._state.adding:
            self.modified_at = timezone.now()
        super().save(force_insert, force_update, using, update_fields)


# Deprecated
class BaseModel(SimpleBaseModel):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=timezone.now, editable=False)


class ParanoidMixin(models.Model):
    class Meta:
        abstract = True

    objects = ParanoidManager()
    deleted = models.BooleanField(default=False, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    deletion_error_cautions = ""

    def pass_delete_validation(self, paranoid, user):
        return True

    def get_deletion_error_message(self):
        msg = _("E1001: %s deletion can't be performed.")
        return msg % (self._meta.verbose_name, self.deletion_error_cautions)

    def get_deletion_message(self):
        msg = _("E1010: %s deleted succesfully.")
        return msg % self._meta.verbose_name

    def delete(self, using=None, keep_parents=False, paranoid=False, user=None):
        """
        Give paranoid delete mechanism to each record
        """
        if not self.pass_delete_validation(paranoid, user):
            raise ValidationError(self.get_deletion_error_message())

        if paranoid:
            self.deleted = True
            self.deleted_at = timezone.now()
            self.save()
        else:
            super().delete(using=using, keep_parents=keep_parents)

    def pass_restore_validation(self):
        return self.deleted

    def get_restoration_error_message(self):
        msg = _("E1002: %s restoration can't be performed.")
        return msg % self._meta.verbose_name

    def restore(self):
        if not self.pass_restore_validation():
            raise ValidationError(self.get_restoration_error_message())
        self.deleted = False
        self.deleted_at = None
        self.save()


class BaseSnippet(SimpleBaseModel):
    """Base snippet"""

    class Meta:
        abstract = True

    objects = SnippetManager()

    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))
    description = models.TextField(null=True, blank=True, max_length=512, verbose_name=_("Description"))

    def __str__(self):
        return self.name

    def natural_key(self):
        key = (self.name,)
        return key
