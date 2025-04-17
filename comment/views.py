from rest_framework import generics
from .models import Comment
from task.models import Task
from .serializers import CommentSerializer
from .permissions import IsTaskParticipant, IsCommentOwnerOrAdmin

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsTaskParticipant]

    def get_parent_task(self):
        task_id = self.kwargs['task_id']
        return Task.objects.get(pk=task_id)

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Comment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task = self.get_parent_task()
        serializer.save(task=task)

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsTaskParticipant, IsCommentOwnerOrAdmin]

    def get_object(self):
        comment = super().get_object()
        self.check_object_permissions(self.request, comment)
        return comment