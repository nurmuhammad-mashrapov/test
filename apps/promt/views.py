from rest_framework import generics
from apps.promt.models import Promt
from apps.promt.serializers import PromttListSerializer, PromtDetailSerializer


class ListPromtView(generics.ListAPIView):
    queryset = Promt.objects.all()
    serializer_class = PromttListSerializer


class DetailPromtView(generics.RetrieveAPIView):
    queryset = Promt.objects.all()
    serializer_class = PromtDetailSerializer
    lookup_field = 'slug'


class OtherPromtView(generics.ListAPIView):
    queryset = Promt.objects.all()
    serializer_class = PromttListSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Promt.objects.all()
        slug = self.kwargs.get('slug')
        # pop slug
        queryset = queryset.exclude(slug=slug)
        return queryset