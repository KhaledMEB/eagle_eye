from django.urls import path
from .views import VehiculeListView

urlpatterns = [
    path('', VehiculeListView.as_view(), name='vehicules-home'),
]