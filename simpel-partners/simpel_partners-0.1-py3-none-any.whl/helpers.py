from .models import Partner


def get_partner_states():
    model_key = "%s.%s" % (Partner._meta.app_label, Partner._meta.model_name)
    states = dict()
    states["count_all"] = Partner.objects.all().count()
    states["count_active"] = Partner.objects.filter(is_active=True).count()
    states["count_verified"] = Partner.objects.filter(is_verified=True).count()
    return {model_key: states}
