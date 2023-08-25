from rest_framework import generics
from apps.advertisement.models import Advertisement
from apps.advertisement.serializers import AdvertisementSerializer


class ListAdvertisementView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    search_fields = ('title',)
