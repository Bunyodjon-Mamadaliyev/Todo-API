from rest_framework import serializers
from .models import TaskHistory
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TaskHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TaskHistory
        fields = ['id', 'task', 'user', 'action', 'timestamp']
