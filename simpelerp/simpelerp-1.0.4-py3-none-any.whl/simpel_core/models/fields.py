from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ObjectDoesNotExist


class CustomGenericForeignKey(GenericForeignKey):
    def __init__(self, ct_field="content_type", fk_field="object_id", pk_field=None, *args, **kwargs):
        self.pk_field = pk_field or "pk"
        super().__init__(ct_field, fk_field, *args, **kwargs)

    def __get__(self, instance, cls=None):
        if instance is None:
            return self

        # Don't use getattr(instance, self.ct_field) here because that might
        # reload the same ContentType over and over (#5570). Instead, get the
        # content type ID here, and later when the actual instance is needed,
        # use ContentType.objects.get_for_id(), which has a global cache.
        f = self.model._meta.get_field(self.ct_field)
        ct_id = getattr(instance, f.get_attname(), None)
        pk_val = getattr(instance, self.fk_field)

        rel_obj = self.get_cached_value(instance, default=None)
        if rel_obj is not None:
            ct_match = ct_id == self.get_content_type(obj=rel_obj, using=instance._state.db).id
            pk_match = getattr(rel_obj, self.pk_field, None) == rel_obj.pk
            if ct_match and pk_match:
                return rel_obj
            else:
                rel_obj = None
        if ct_id is not None:
            ct = self.get_content_type(id=ct_id, using=instance._state.db)
            try:
                filters = {self.pk_field: pk_val}
                rel_obj = ct.get_object_for_this_type(**filters)
            except ObjectDoesNotExist:
                pass
        self.set_cached_value(instance, rel_obj)
        return rel_obj

    def __set__(self, instance, value):
        ct = None
        fk = None
        # Get fk value by self.pk_field name
        if value is not None:
            ct = self.get_content_type(obj=value)
            fk = getattr(value, self.pk_field)

        setattr(instance, self.ct_field, ct)
        setattr(instance, self.fk_field, fk)
        self.set_cached_value(instance, value)
