from rest_framework import serializers
from apps.advertisement.models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'image', 'link', 'is_active', 'order')
        ref_name = 'AdvertisementModel'

