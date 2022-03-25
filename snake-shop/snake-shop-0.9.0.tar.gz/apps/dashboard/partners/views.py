from django.contrib.auth.models import Permission
from oscar.apps.dashboard.partners import views as partner_views


class PartnerUserLinkView(partner_views.PartnerUserLinkView):
    """
    Remove automatically created dashboard permission
    """
    def link_user(self, user, partner):
        result = partner_views.PartnerUserLinkView.link_user(
            self, user, partner)
        dashboard_access_perm = Permission.objects.get(
                codename='dashboard_access',
                content_type__app_label='partner')
        user.user_permissions.remove(dashboard_access_perm)
        return result
