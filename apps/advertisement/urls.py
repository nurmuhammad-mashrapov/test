from django.urls import path
from apps.advertisement.views import ListAdvertisementView




urlpatterns = [
    path('list/', ListAdvertisementView.as_view(), name='list')
]