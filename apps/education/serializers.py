from rest_framework import serializers
from apps.education.models import Education


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('title', 'description', 'image', 'order', 'is_active', 'slug')

