from rest_framework import permissions

class IsConductorOrAdminOrReadOnly(permissions.BasePermission):
    message = "User must be an admin or conductor to modify the jam session members."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

        return request.user == obj.conductor
