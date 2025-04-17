from rest_framework import permissions


class IsTaskOwnerOrAssigned(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.assigned_to.all() or request.user == obj.created_by
        return request.user == obj.created_by


class IsAuthenticatedForListing(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' and view.action in ['list', 'retrieve']:
            return request.user.is_authenticated
        return True

