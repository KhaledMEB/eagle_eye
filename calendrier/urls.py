from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('calendar/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]