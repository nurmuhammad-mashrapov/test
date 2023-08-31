from rest_framework import serializers
from apps.promt.models import Promt


class PromttListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promt
        fields = ('title', 'description_ru', 'category', 'order', 'is_active', 'slug')


class PromtDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promt
        fields = ('title', 'description_ru', 'description_en', 'slug')
