from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        ref_name = 'TaskUserSerializer'

class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    created_by = UserSerializer(read_only=True)
    assigned_users = UserSerializer(many=True, read_only=True, source='assigned_to')
    subtasks_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    attachments_count = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'priority', 'status',
                    'category', 'category_name', 'created_by', 'assigned_users',
                    'deadline', 'created_at', 'updated_at', 'is_recurring',
                    'recurrence_pattern', 'estimated_hours', 'actual_hours',
                    'subtasks_count', 'comments_count', 'attachments_count'
                ]
        read_only_fields = [
            'id', 'created_at', 'updated_at', 'created_by',
            'subtasks_count', 'comments_count', 'attachments_count'
        ]

    def get_subtasks_count(self, obj):
        return obj.subtasks.count() if hasattr(obj, 'subtasks') else 0

    def get_comments_count(self, obj):
        return obj.comments.count() if hasattr(obj, 'comments') else 0

    def get_attachments_count(self, obj):
        return obj.attachments.count() if hasattr(obj, 'attachments') else 0

    def to_representation(self, instance):
        data = super().to_representation(instance)

        for field in ['deadline', 'created_at', 'updated_at']:
            if data.get(field):
                dt = instance.__getattribute__(field)
                data[field] = dt.isoformat().replace('+00:00', 'Z')

        for field in ['estimated_hours', 'actual_hours']:
            if data[field] is not None:
                data[field] = float(data[field])

        if data['recurrence_pattern'] is None:
            data['recurrence_pattern'] = None

        return data
