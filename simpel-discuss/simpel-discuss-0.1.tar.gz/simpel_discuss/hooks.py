import simpel_hookup.core as hookup

from .viewsets import ThreatViewSet


@hookup.register("REGISTER_DASHBOARD_VIEWSET")
def register_web_cooment_viewsets():
    return ThreatViewSet
