from django.urls import path
from .views import SubTaskListCreateView, SubTaskRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/<int:task_id>/subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-retrieve-update-destroy'),
]