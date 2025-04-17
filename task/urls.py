from django.urls import path
from .views import (
    TaskListCreateView, TaskRetrieveUpdateDestroyView,
    TaskByStatusView, TaskByPriorityView, TaskByCategoryView,
    AssignedToMeView, CreatedByMeView, OverdueTasksView,
    DueTodayTasksView, TaskSearchView
)

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('tasks/by-status/<str:status>/', TaskByStatusView.as_view(), name='task-by-status'),
    path('tasks/by-priority/<str:priority>/', TaskByPriorityView.as_view(), name='task-by-priority'),
    path('tasks/by-category/<int:category_id>/', TaskByCategoryView.as_view(), name='task-by-category'),
    path('tasks/assigned-to-me/', AssignedToMeView.as_view(), name='task-assigned-to-me'),
    path('tasks/created-by-me/', CreatedByMeView.as_view(), name='task-created-by-me'),
    path('tasks/overdue/', OverdueTasksView.as_view(), name='task-overdue'),
    path('tasks/due-today/', DueTodayTasksView.as_view(), name='task-due-today'),
    path('tasks/search/', TaskSearchView.as_view(), name='task-search'),
]