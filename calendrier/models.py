from django.db import models
from vehicules.models import Vehicule
import datetime
from django.urls import reverse
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField(default=datetime.date.today)
    def __str__(self):
        return self.title
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'
class employees(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class maintenance(models.Model):
    date = models.DateTimeField(default=datetime.date.today)
    employee = models.ForeignKey(employees,on_delete=models.CASCADE)
    voiture = models.ForeignKey(Vehicule,on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    @property
    def get_html_url(self):
        url = reverse('post-detail', kwargs={'pk': self.pk})
        return f'<a href="{url}" class="badge-dark">{self.titre}</a>'
    def __str__(self):
        return self.titre



