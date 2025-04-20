from rest_framework import generics
from .models import Comment
from task.models import Task
from .serializers import CommentSerializerV1, CommentSerializerV2
from .permissions import IsTaskParticipant, IsCommentOwnerOrAdmin

class CommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsTaskParticipant]

    def get_serializer_class(self):
        if self.request.version == "1":
            return CommentSerializerV1
        return CommentSerializerV2

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
    permission_classes = [IsTaskParticipant, IsCommentOwnerOrAdmin]
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.version == "1":
            return CommentSerializerV1
        return CommentSerializerV2

    def get_object(self):
        comment = super().get_object()
        self.check_object_permissions(self.request, comment)
        return comment