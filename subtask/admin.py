from django.contrib import admin
from .models import SubTask

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description', 'task__title')
    readonly_fields = ('created_at', 'updated_at')
