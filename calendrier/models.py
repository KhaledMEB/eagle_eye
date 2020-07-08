from django.db import models
from vehicules.models import Vehicule
import datetime
from django.urls import reverse

class employees(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class etat(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class maintenance(models.Model):
    date = models.DateTimeField(default=datetime.date.today)
    employee = models.ForeignKey(employees,on_delete=models.CASCADE)
    voiture = models.ForeignKey(Vehicule,on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    etat = models.ForeignKey(etat,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200)
    observation = models.CharField(max_length=200)
    @property
    def get_html_url(self):
        url = reverse('post-detail', kwargs={'pk': self.pk})
        d = ''
        if self.etat.name=="en cours":
            d += f'<a href="{url}" class="badge-dark"> {self.titre} </li>'
        elif self.etat.name=="terminé":
            d += f'<a href="{url}" class="badge-success"> {self.titre} </li>'
        else:
            d += f'<a href="{url}" class="badge-danger"> {self.titre} </li>' 
        return d
    def __str__(self):
        return self.titre



