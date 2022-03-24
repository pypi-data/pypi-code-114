from django.urls import include, path
from django.utils.translation import gettext_lazy as _

from simpel_routers.viewsets import ReadOnlyViewSet, login_required_m

from .models import Threat


class ThreatViewSet(ReadOnlyViewSet):
    model = Threat
    filterset_fields = ["comment"]
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    @login_required_m
    def index_view(self, request):
        self.request = request
        kwargs = {
            "viewset": self,
            "title": _("My Discuss"),
        }
        view_class = self.index_view_class
        return view_class.as_view(**kwargs)(request)

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path("comments/", include("django_comments_xtd.urls"))
        ]
        return urls
