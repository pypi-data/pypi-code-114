from django.utils.translation import gettext_lazy as _

from simpel.simpel_products.models import Group, Product
from simpel.simpel_projects.models import Task


class CertificationService(Product):

    doc_prefix = "PRO"

    class Meta:
        db_table = "simpel_certification_service"
        verbose_name = _("Product Certification")
        verbose_name_plural = _("Product Certifications")
        permissions = (
            ("export_certificationservice", _("Can export Certification Service")),
            ("import_certificationservice", _("Can import Certification Service")),
        )

    def get_doc_prefix(self):
        return "PRO"

    def save(self, *args, **kwargs):
        self.is_partial = False
        self.is_sellable = True
        if self.group is None:
            self.group = Group.get_or_create("PRO", "Product Certification")
        if self.is_deliverable is None:
            self.is_deliverable = True
        return super().save(*args, **kwargs)


class CertificationTask(Task):
    class Meta:
        db_table = "simpel_certification_task"
        verbose_name = _("Certification Task")
        verbose_name_plural = _("Certification Task")
