from django.urls import path
from . views import *


# class MidjouneyList(generics.ListCreateAPIView):
#     queryset = Midjouney.objects.all()
#     serializer_class = MidjouneySerializer
#
#
# class StrukturaList(generics.ListCreateAPIView):
#     queryset = Struktura.objects.all()
#     serializer_class = StrukturaSerializer
#
#
# class ParametrList(generics.ListCreateAPIView):
#     queryset = Parametr.objects.all()
#     serializer_class = ParametrSerializer


urlpatterns = [
    path('midjouney/', MidjouneyList.as_view()),
    path('struktura/', StrukturaList.as_view()),
    path('parametr/', ParametrList.as_view())
]
