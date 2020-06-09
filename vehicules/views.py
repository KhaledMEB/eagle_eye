from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>La Liste des Vehicules</h1>')