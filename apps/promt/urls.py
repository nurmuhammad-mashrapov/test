from django.urls import path
from apps.promt.views import ListPromtView, DetailPromtView, OtherPromtView

urlpatterns = [
    path('list/', ListPromtView.as_view(), name='list'),
    path('detail/<slug:slug>/', DetailPromtView.as_view(), name='detail'),
    path('other/<slug:slug>/', OtherPromtView.as_view(), name='other')
]