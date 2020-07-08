from django.urls import path
from .views import VehiculeListView, VehiculeDetailsView, VehiculeCreateView, VehiculeUpdateView

urlpatterns = [
    path('', VehiculeListView.as_view(), name='vehicules-home'),
    path('vehicule/<int:pk>', VehiculeDetailsView.as_view(), name='vehicule-detail'),
    path('new/', VehiculeCreateView.as_view(), name='vehicule-create'),
    path('vehicule/<int:pk>/update', VehiculeUpdateView.as_view(), name='vehicule-update'),

]