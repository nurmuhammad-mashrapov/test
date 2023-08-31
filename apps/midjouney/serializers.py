from rest_framework import serializers
from apps.midjouney.models import Midjouney, Struktura, Parametr, ImageParametr



class MidjouneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Midjouney
        fields = ('zapros', 'otvet')



class StrukturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Struktura
        fields = ('zapros', 'otvet')



class ImageParametrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageParametr
        fields = ('otvet',)




class ParametrSerializer(serializers.ModelSerializer):
    image = ImageParametrSerializer(read_only=True)
    class Meta:
        model = Parametr
        fields = ('zapros', 'image')





