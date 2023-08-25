from rest_framework import generics, filters
from django.db.models import Q
from django_filters import rest_framework as django_filters
from apps.neauralnetwork.models import NeuralNetwork
from apps.neauralnetwork.serializers import NeuralNetworkSerializer


class NeuralNetworkFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title")
    zadacha = django_filters.CharFilter(field_name="zadacha")
    paid = django_filters.BooleanFilter(field_name="paid")
    trial = django_filters.BooleanFilter(field_name="trial")
    tag = django_filters.CharFilter(method='filter_by_tag')

    def filter_by_tag(self, queryset, name, value):
        return queryset.filter(tag=value)

    class Meta:
        model = NeuralNetwork
        fields = ('title', 'zadacha', 'paid', 'trial', 'tag')


class NeuralNetworkListView(generics.ListAPIView):
    queryset = NeuralNetwork.objects.all()
    serializer_class = NeuralNetworkSerializer
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = NeuralNetworkFilter
    search_fields = ("title",)


class NeuralNetworkDetailView(generics.RetrieveAPIView):
    queryset = NeuralNetwork.objects.all()
    serializer_class = NeuralNetworkSerializer
    lookup_field = 'slug'
    lookup_url_kwarg ='slug'

    def get_object(self):
        slug = self.kwargs['slug']
        return NeuralNetwork.objects.get(slug=slug)


class SimilarNeuralNetworkListView(generics.ListAPIView):
    serializer_class = NeuralNetworkSerializer

    def get_queryset(self):
        queryset = NeuralNetwork.objects.all()
        slug = self.kwargs['slug']
        neural_network = NeuralNetwork.objects.get(slug=slug)
        tag = neural_network.tag.all()
        queryset = queryset.filter(tag__in=tag).exclude(slug=slug).order_by('order')
        return queryset



