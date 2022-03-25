from oscarapi.views import root as base_root
from rest_framework.decorators import api_view
from django.conf import settings
import collections
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .sync import VIEWSETS


def SYNC_APIS(r, f):
    apis = []
    for viewset_class in VIEWSETS:
        basename = viewset_class().base_name
        list_urlname = viewset_class().list_url
        apis.append((
            basename, reverse(list_urlname, request=r, format=f)
        ))
    return apis


@api_view(("GET",))
def api_root(
    request, format=None, *args, **kwargs
):  # pylint: disable=redefined-builtin
    """
    GET:
    Display all available urls.

    Since some urls have specific permissions, you might not be able to access
    them all.
    """
    apis = base_root.PUBLIC_APIS(request, format)

    if (
        not getattr(settings, "OSCARAPI_BLOCK_ADMIN_API_ACCESS", True)
        and request.user.is_staff
    ):
        apis += [
            (
                "admin",
                collections.OrderedDict(base_root.ADMIN_APIS(request, format))
            )
        ]
    apis += [("sync", collections.OrderedDict(SYNC_APIS(request, format)))]
    return Response(collections.OrderedDict(apis))
