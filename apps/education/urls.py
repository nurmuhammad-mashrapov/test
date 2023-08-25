from django.urls import path
from apps.education.views import ListEducationView

urlpatterns = [
    path('list/', ListEducationView.as_view(), name='list')
]