from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'vehicules/home.html', {'title': 'Véhicules'})