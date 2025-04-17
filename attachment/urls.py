from django.urls import path
from .views import TaskAttachmentListCreateView, AttachmentRetrieveDestroyView

urlpatterns = [
    path('tasks/<int:id>/attachments/', TaskAttachmentListCreateView.as_view(), name='task-attachments'),
    path('attachments/<int:pk>/', AttachmentRetrieveDestroyView.as_view(), name='attachment-detail'),
]
