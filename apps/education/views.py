from rest_framework import generics
from apps.education.models import Education
from apps.education.serializers import AdvertisementSerializer


class ListEducationView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = AdvertisementSerializer
    search_fields = ('title',)
