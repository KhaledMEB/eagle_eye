from django.db import models
from vehicules.models import Vehicule
import datetime
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=datetime.date.today)
    def __str__(self):
        return self.title
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<p>{self.title}</p><a href="{url}">edit</a>'
class employees(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.title
class maintenance(models.Model):
    date = models.DateTimeField(default=datetime.date.today)
    employee = models.ForeignKey(employees,on_delete=models.CASCADE)
    voiture = models.ForeignKey(Vehicule,on_delete=models.CASCADE)
    titre = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<p>{self.title}</p><a href="{url}">edit</a>'
    def __str__(self):
        return self.title



