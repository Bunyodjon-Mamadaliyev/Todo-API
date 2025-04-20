from rest_framework import generics, permissions
from .models import Attachment
from .serializers import AttachmentSerializerV1, AttachmentSerializerV2
from .permissions import IsTaskAssigneeOrOwner

class TaskAttachmentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsTaskAssigneeOrOwner]

    def get_serializer_class(self):
        if self.request.version == "1":
            return AttachmentSerializerV1
        return AttachmentSerializerV2

    def get_queryset(self):
        task_id = self.kwargs['id']
        return Attachment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs['id']
        serializer.save(uploaded_by=self.request.user, task_id=task_id)


class AttachmentRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Attachment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.version == "1":
            return AttachmentSerializerV1
        return AttachmentSerializerV2
