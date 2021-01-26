from rest_framework import permissions


class IsSelfOrIsOwnerOrIsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if view.__class__.__name__ in ['ArticleViewSet', 'CommentViewSet']:
            user = obj.created_by
        else:
            user = obj

        return bool(
            user == request.user
        )

