from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from .models import Task
from .serializers import TaskSerializer
from common.permissions import IsTaskOwnerOrAssigned, IsAuthenticatedForListing

User = get_user_model()

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'priority', 'category']
    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTaskOwnerOrAssigned]

class TaskByStatusView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        status = self.kwargs['status']
        return Task.objects.filter(
            status=status,
            assigned_to=self.request.user
        )

class TaskByPriorityView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        priority = self.kwargs['priority']
        return Task.objects.filter(
            priority=priority,
            assigned_to=self.request.user
        )

class TaskByCategoryView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Task.objects.filter(
            category_id=category_id,
            assigned_to=self.request.user
        )

class AssignedToMeView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

class CreatedByMeView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

class OverdueTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        from django.utils import timezone
        return Task.objects.filter(
            deadline__lt=timezone.now(),
            status__in=['todo', 'in_progress'],
            assigned_to=self.request.user
        )

class DueTodayTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        from django.utils import timezone
        today = timezone.now().date()
        return Task.objects.filter(
            deadline__date=today,
            assigned_to=self.request.user
        )

class TaskSearchView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)