from rest_framework import permissions


class isAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # for readonly
        if request.method in permissions.SAFE_METHODS:
            return True
        # for author to edit
        return obj.author == request.user