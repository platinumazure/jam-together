from rest_framework import permissions
from .models import JamSession

class IsConductorOrAdminOrReadOnly(permissions.BasePermission):
    message = "User must be an admin or conductor."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True

        if request.method == "POST" and "jam_session" in request.data:
            try:
                jam_session = JamSession.objects.get(pk=request.data["jam_session"]["id"])
            except JamSession.DoesNotExist:
                return True
            else:
                return jam_session.conductor == request.user

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

        if hasattr(obj, "conductor"):
            return request.user == obj.conductor
        elif hasattr(obj, "jam_session"):
            return request.user == obj.jam_session.conductor
        else:
            return False


class IsAdminOrReadOnly(permissions.BasePermission):
    message = "User must be an admin."

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff


class IsReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
