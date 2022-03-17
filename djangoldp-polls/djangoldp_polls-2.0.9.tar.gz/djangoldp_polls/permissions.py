from djangoldp.permissions import LDPPermissions
from djangoldp.utils import is_authenticated_user
from djangoldp_polls.filters import PollFilterBackend
from djangoldp_polls.models.poll import Response

# class ResponsePermissions(LDPPermissions):
# 	with_cache = False
#
# 	def get_object_permissions(self, request, view, obj):
# 		perms = super().get_object_permissions(request, view, obj)
#
# 		return {}
#
#
# 	def get_container_permissions(self, request, view, obj=None):
# 		perms = super().get_container_permissions(request, view, obj)
# 		perms.remove('inherit')
#
# 		return perms



