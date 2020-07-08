from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Vehicule

#def home(request):
#    return render(request, 'vehicules/home.html', {'title': 'Véhicules'})


# class based view
class VehiculeListView(ListView):
    model = Vehicule
    template_name = 'vehicules/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'vehicules'
    # paginator : 10 pages per page
    paginate_by = 10

class VehiculeDetailsView(DetailView):
    model = Vehicule

class VehiculeCreateView(CreateView):
    model = Vehicule
    fields = '__all__'
    
class VehiculeUpdateView(UpdateView):
    model = Vehicule
    fields = '__all__'
    success_url = '/vehicules'