from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'text', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('text', 'user__username', 'task__title')
    readonly_fields = ('created_at', 'updated_at')
