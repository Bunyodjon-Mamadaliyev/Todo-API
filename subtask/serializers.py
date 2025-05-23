from rest_framework import serializers
from .models import SubTask

class SubTaskSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'task', 'title', 'description', 'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        for field in ['created_at', 'updated_at']:
            if data.get(field):
                dt = instance.__getattribute__(field)
                data[field] = dt.isoformat().replace('+00:00', 'Z')
        return data

class SubTaskSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id', 'task',
                  'title_uz',
                  'title_en',
                  'title_ru',
                  'description_uz',
                  'description_en',
                  'description_ru',
                  'is_completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        for field in ['created_at', 'updated_at']:
            if data.get(field):
                dt = instance.__getattribute__(field)
                data[field] = dt.isoformat().replace('+00:00', 'Z')
        return data