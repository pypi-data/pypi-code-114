from django import forms
from django.utils.translation import gettext_lazy as _
from import_export.formats import base_formats
from import_export.forms import ExportForm

EXPORT_DATASETS = (
    ("sales_order", _("Sales Order")),
    ("sales_quotation", _("Sales Quotation")),
    ("invoice", _("Invoices")),
    ("final_document", "Final Documents"),
)


class ExportFormStep1(ExportForm):
    def __init__(self, *args, **kwargs):
        default_formats = base_formats.DEFAULT_FORMATS
        formats = [f for f in default_formats if f().can_import()]
        super().__init__(formats, *args, **kwargs)
        self.fields["dataset"] = forms.ChoiceField(choices=EXPORT_DATASETS)


class ExportFormStep2(forms.Form):
    """Choose ordering and fields"""

    message = forms.CharField(widget=forms.Textarea)


EXPORT_WIZARD_FORMS = [
    ("export_step1", ExportFormStep1),
    ("export_step2", ExportFormStep2),
]

EXPORT_WIZARD_TEMPLATES = {
    "export_step1": "reports/wizard.html",
    "export_step2": "reports/wizard.html",
}
