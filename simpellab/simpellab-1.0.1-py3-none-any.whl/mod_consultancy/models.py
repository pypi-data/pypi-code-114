from django.utils.translation import gettext_lazy as _

from simpel.simpel_products.models import Group, Product


class ConsultancyService(Product):

    doc_prefix = "KSL"

    class Meta:
        db_table = "simpel_consultancy_service"
        verbose_name = _("Consultancy Service")
        verbose_name_plural = _("Consultancy Services")
        permissions = (
            ("export_consultancyservice", _("Can export Consultancy Service")),
            ("import_consultancyservice", _("Can import Consultancy Service")),
        )

    def get_doc_prefix(self):
        return "KSL"

    def save(self, *args, **kwargs):
        self.is_partial = False
        self.is_sellable = True
        if self.group is None:
            self.group = Group.get_or_create("KSL", "Consultancy")
        if self.is_deliverable is None:
            self.is_deliverable = True
        return super().save(*args, **kwargs)
