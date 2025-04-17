from django.urls import path
from .views import TaskHistoryListView

urlpatterns = [
    path('tasks/<int:id>/history/', TaskHistoryListView.as_view(), name='task-history'),
]
