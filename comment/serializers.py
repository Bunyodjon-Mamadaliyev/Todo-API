from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'task', 'user', 'text', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field in ['created_at', 'updated_at']:
            if data.get(field):
                dt = instance.__getattribute__(field)
                data[field] = dt.isoformat().replace('+00:00', 'Z')
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)