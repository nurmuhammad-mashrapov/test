from rest_framework import serializers
from apps.neauralnetwork.models import NeuralNetwork, Tag




class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag  # Замените на имя вашей модели для тегов
        fields = ('title',)  # Замените на поле, содержащее название тега


class NeuralNetworkSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    class Meta:
        model = NeuralNetwork
        fields = ('title', 'link', 'description', 'zadacha', 'tag', 'image','dostup', 'icon_18', 'icon_ru', 'slug', 'order')
