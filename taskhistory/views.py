from rest_framework import generics, permissions
from .models import TaskHistory
from .serializers import TaskHistorySerializer

class TaskHistoryListView(generics.ListAPIView):
    serializer_class = TaskHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs['id']
        return TaskHistory.objects.filter(task__id=task_id)


