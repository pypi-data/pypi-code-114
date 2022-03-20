from django.contrib import admin
from django.urls import reverse

from simpel.simpel_admin.base import AdminView


class AdminProfileUpdateView(AdminView):
    def get_success_url(self):
        return reverse("admin:admin_profile")

    def get_context_data(self, **kwargs):
        kwargs.update(
            {
                "user": self.request.user,
                "forms": self.get_forms(),
                "form_action_url": reverse("admin:admin_profile"),
                **admin.site.each_context(self.request),
            }
        )
        return kwargs
