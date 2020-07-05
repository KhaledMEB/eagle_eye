from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
import django.views.generic.dates
from django.urls import reverse_lazy,reverse
from .utils import Calendar
from .models import Event
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
import calendar
from django.shortcuts import get_object_or_404
from .form import EventForm
def event_view(request):
    return render(request, 'calendrier/event.html', {'title': 'event'})
def day_view(request):
    return render(request, 'calendrier/day.html', {'title': 'event'})

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
class CalendarView(ListView):
    model = Event
    template_name = 'calendrier/calendar.html'
    success_url = reverse_lazy("calendar")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        #events = Event.objects.filter(start_time__year=Calendar.year, start_time__month=Calendar.month)
        #html_day = cal.formatday(d,events)
        #context['day'] = mark_safe(html_day)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'calendrier/event.html', {'form': form})