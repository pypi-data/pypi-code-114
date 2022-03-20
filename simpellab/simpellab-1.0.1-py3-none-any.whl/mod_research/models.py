from django.utils.translation import gettext_lazy as _

from simpel.simpel_products.models import Group, Product


class ResearchService(Product):
    
    doc_prefix = "LIB"

    class Meta:
        db_table = "simpel_research_service"
        verbose_name = _("Research and Development")
        verbose_name_plural = _("Research and Developments")
        permissions = (
            ("export_researchservice", _("Can export Research Service")),
            ("import_researchservice", _("Can import Research Service")),
        )

    def get_doc_prefix(self):
        return "LIB"

    def save(self, *args, **kwargs):
        self.is_partial = False
        self.is_sellable = True
        if self.group is None:
            self.group = Group.get_or_create("LIB", "Research")
        if self.is_deliverable is None:
            self.is_deliverable = True
        return super().save(*args, **kwargs)
