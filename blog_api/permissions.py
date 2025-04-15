from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only authenticated users can see the list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permission is allowed for any request, so we will always
        # allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only the author of the message or the administrator have write permissions.
        return obj.author == request.user or request.user.is_staff