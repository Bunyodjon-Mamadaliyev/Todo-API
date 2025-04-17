from rest_framework import generics, permissions
from .models import Attachment
from .serializers import AttachmentSerializer
from .permissions import IsTaskAssigneeOrOwner

class TaskAttachmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsTaskAssigneeOrOwner]

    def get_queryset(self):
        task_id = self.kwargs['id']
        return Attachment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['id']
        serializer.save(uploaded_by=self.request.user, task_id=task_id)


class AttachmentRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticated]
