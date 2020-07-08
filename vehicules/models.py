from django.db import models
from django.urls import reverse

class Vehicule(models.Model):
    STATUT_CHOICES = (
    ('Actif', 'Actif'),
    ('En Atelier', 'En Atelier'),
    ('En Panne', 'En Panne'),
    ('Hors Service', 'Hors Service'),
)
    TYPE_CHOICES = (
    ('Voiture', 'Voiture'),
    ('Camion', 'Camion'),
    ('Moto', 'Moto'),
)
    GROUPE_CHOICES = (
    ('Civil', 'Civil'),
    ('Militaire', 'Militaire'),
)
    nom = models.CharField(max_length=100)
    vip = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    groupe = models.CharField(max_length=20, choices=GROUPE_CHOICES)
    compteur = models.IntegerField()
    conducteur = models.CharField(max_length=40)
    image = models.ImageField(default='default.jpg', upload_to='vehicules_pics')
    def __str__(self):
        return self.nom