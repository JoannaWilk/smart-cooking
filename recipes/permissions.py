from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow to edit an object only a user who added it.
    """

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request,
        # so we always allow GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the user who added an object
        return obj.added_by == request.user
