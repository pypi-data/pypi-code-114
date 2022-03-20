from django.contrib import admin
from django.urls import path

from .forms import EXPORT_WIZARD_FORMS
from .models import ReportLog
from .views import ExportWizardView


@admin.register(ReportLog)
class ReportLogAdmin(admin.ModelAdmin):
    list_display = ["created_at", "user", "dataname", "file"]
    change_list_template = "reports/change_list.html"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False

    def export_wizard(self, request):
        """Run export wizzard view"""
        return ExportWizardView.as_view(EXPORT_WIZARD_FORMS)(request)

    def get_urls(self):
        super_urls = super().get_urls()
        urls = [
            path("export_wizzard/", self.export_wizard, name="report_export_wizard"),
        ]
        urls += super_urls
        return urls
