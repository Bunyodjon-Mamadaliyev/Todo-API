from rest_framework import permissions

class IsTaskOwnerOrAssigned(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(view, 'get_parent_task'):
            task = view.get_parent_task()
            return request.user in task.assigned_to.all() or request.user == task.created_by
        return True

    def has_object_permission(self, request, view, obj):
        return (request.user in obj.task.assigned_to.all() or
                request.user == obj.task.created_by)

class IsTaskOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user == obj.task.created_by
        return True