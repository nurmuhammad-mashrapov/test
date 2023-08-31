from rest_framework import generics
from apps.midjouney.models import Midjouney, Struktura, Parametr, ImageParametr
from apps.midjouney.serializers import MidjouneySerializer, StrukturaSerializer, ParametrSerializer




class MidjouneyList(generics.ListCreateAPIView):
    queryset = Midjouney.objects.all()
    serializer_class = MidjouneySerializer



class StrukturaList(generics.ListCreateAPIView):
    queryset = Struktura.objects.all()
    serializer_class = StrukturaSerializer


class ParametrList(generics.ListCreateAPIView):
    queryset = Parametr.objects.all()
    serializer_class = ParametrSerializer


