from rest_framework import serializers
from .models import Attachment
from django.contrib.auth.models import User

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AttachmentSerializerV1(serializers.ModelSerializer):
    uploaded_by = UserInfoSerializer(read_only=True)
    file = serializers.FileField(use_url=True)

    class Meta:
        model = Attachment
        fields = ['id', 'task', 'file', 'filename', 'file_type', 'uploaded_by', 'uploaded_at',]

class AttachmentSerializerV2(serializers.ModelSerializer):
    uploaded_by = UserInfoSerializer(read_only=True)
    file = serializers.FileField(use_url=True)

    class Meta:
        model = Attachment
        fields = ['id',
                  'task_uz',
                  'task_en',
                  'task_ru',
                  'file',
                  'filename_uz',
                  'filename_en',
                  'filename_ru',
                  'file_type', 'uploaded_by', 'uploaded_at',]
