from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'position', 'phone')
    search_fields = ('user__username', 'department', 'position', 'phone')
    list_filter = ('department', 'position')

admin.site.register(UserProfile, UserProfileAdmin)
