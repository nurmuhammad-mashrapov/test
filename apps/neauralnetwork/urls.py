from django.urls import path
from apps.neauralnetwork.views import NeuralNetworkListView, SimilarNeuralNetworkListView, NeuralNetworkDetailView


urlpatterns = [
    path('list/', NeuralNetworkListView.as_view()),
    path('detail/<slug:slug>/', NeuralNetworkDetailView.as_view()),
    path('list/similar/<slug:slug>/', SimilarNeuralNetworkListView.as_view()),
]