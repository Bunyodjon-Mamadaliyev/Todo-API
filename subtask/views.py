from rest_framework import generics, permissions
from .models import SubTask
from task.models import Task
from .serializers import SubTaskSerializer
from .permissions import IsTaskOwnerOrAssigned, IsTaskOwner

class SubTaskListCreateView(generics.ListCreateAPIView):
    serializer_class = SubTaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsTaskOwnerOrAssigned]

    def get_parent_task(self):
        task_id = self.kwargs['task_id']
        return Task.objects.get(pk=task_id)

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return SubTask.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task = self.get_parent_task()
        serializer.save(task=task)

class SubTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsTaskOwnerOrAssigned, IsTaskOwner]

    def get_object(self):
        subtask = super().get_object()
        self.check_object_permissions(self.request, subtask)
        return subtask