from rest_framework import serializers
from .models import Category

class CategorySerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'color', 'icon', 'created_at']
        read_only_fields = ['id', 'created_at']

class CategorySerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id',
                  'name_uz',
                  'name_en',
                  'name_ru',
                  'description_uz',
                  'description_en',
                  'description_ru',
                  'color', 'icon', 'created_at']
        read_only_fields = ['id', 'created_at']

