from rest_framework import permissions
from task.models import Task

class IsTaskAssigneeOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        task_id = view.kwargs.get('id')
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return False

        return request.user == task.created_by or request.user == task.assigned_to
