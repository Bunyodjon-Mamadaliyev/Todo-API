from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'icon', 'created_at')
    search_fields = ('name', 'description', 'icon')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

