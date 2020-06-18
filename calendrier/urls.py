from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='calendrier-home'),
    path('', views.CalendarView.as_view(), name='calendar'),
]