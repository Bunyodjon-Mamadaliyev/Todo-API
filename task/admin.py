from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'category', 'created_by', 'deadline', 'is_recurring')
    list_filter = ('priority', 'status', 'category', 'is_recurring')
    search_fields = ('title', 'description', 'created_by__username', 'assigned_to__username')
    readonly_fields = ('created_at', 'updated_at')
