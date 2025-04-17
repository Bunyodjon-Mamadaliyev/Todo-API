from rest_framework import serializers
from .models import Attachment
from django.contrib.auth.models import User

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_by = UserInfoSerializer(read_only=True)
    file = serializers.FileField(use_url=True)

    class Meta:
        model = Attachment
        fields = ['id', 'task', 'file', 'filename', 'file_type', 'uploaded_by', 'uploaded_at',]
