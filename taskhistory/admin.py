from django.contrib import admin
from .models import TaskHistory

@admin.register(TaskHistory)
class TaskHistoryAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'action', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('action', 'task__title', 'user__username')
    readonly_fields = ('timestamp',)
