from rest_framework import permissions


class IsOwnerOrNoAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check & return true/false
        return obj.user == request.user
