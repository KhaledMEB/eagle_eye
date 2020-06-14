from django.db import models

class Vehicule(models.Model):
    nom = models.CharField(max_length=100)
    vip = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20)
    statut = models.CharField(max_length=20)
    type_v = models.CharField(max_length=20)
    groupe = models.CharField(max_length=20)
    compteur = models.IntegerField()
    conducteur = models.CharField(max_length=40)