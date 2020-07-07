from datetime import datetime, timedelta
from calendar import HTMLCalendar
from django.urls import reverse

import calendar
from .models import maintenance
class Calendar(HTMLCalendar):
    day_abbr=["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"]
    month_name=["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
    def formatday(self, day, events):
        events_per_day = events.filter(date__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li class="calendar_list badge badge-dark"> {event.get_html_url} </li>'
        if day != 0:
            #url=reverse('day_view', args=('{self.year}-{self.month}-{day}'))
            
            return "<td class='btn-light btn-sm'><span class='date'>%s</span><ul  > %s </ul></td>" %(
                day,d
            )
        return '<td></td>'
    def formatdayevents(self,day,events):
        events_per_day = events.filter(date__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li class="calendar_list"> {event.get_html_url} </li>'
        if day != 0:
            url=reverse('day_view')
            return "<td ><span class='date'><form action='%s'><input type='hidden' value='%s'><input type='submit' value='%s'>  </form></span><ul> %s </ul></td>" %(
                url,day,day,d
            )
        return '<td></td>'
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr class=""> {week} </tr>'
    def formatmonthname(self,theyear,themonth,withyear):
        if withyear:
            s = '%s %s' % (self.month_name[themonth-1], theyear)
        else:
            s = '%s' % self.month_name[themonth-1]
        return '<tr><th colspan="7" class="%s">%s</th></tr>' % (
            self.cssclass_month_head, s)
    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return '<th class="%s btn-light">%s</th>' % (
            self.cssclasses_weekday_head[day], self.day_abbr[day])
    def formatmonth(self, withyear=True):
        events = maintenance.objects.filter(date__year=self.year, date__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar-table calendar table table-borderless table-condensed table-tight "><thead class="btn-primary btn-lg text-center"><p class="text-primary m-0 font-weight-bold"></p>\n'
        cal += f'{self.formatmonthname(self.year, self.month,withyear=withyear)}\n'
        cal+=f'</thead>'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        cal+=f'</table>'
        return cal