from rest_framework import serializers
from apps.neauralnetwork.models import NeuralNetwork


class NeuralNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeuralNetwork
        fields = ('title', 'link', 'description', 'zadacha', 'tag', 'image', 'icon_18', 'icon_ru', 'slug', 'order')