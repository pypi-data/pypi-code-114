from rest_framework.permissions import BasePermission


class AttributeSetPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.has_perm('attributes.view_attributeset')
        elif request.method == 'PUT':
            return request.user.has_perms([
                'subjects.change_subject',
                'attributes.change_attributeset'
            ])
