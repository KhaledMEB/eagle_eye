from django.db import models

class Vehicule(models.Model):
    STATUT_CHOICES = (
    ('AC', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)
    
    nom = models.CharField(max_length=100)
    vip = models.CharField(max_length=100)
    matricule = models.CharField(max_length=20)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    type = models.CharField(max_length=20)
    groupe = models.CharField(max_length=20)
    compteur = models.IntegerField()
    conducteur = models.CharField(max_length=40)
    image = models.ImageField(default='default.jpg', upload_to='vehicules_pics')
    def __str__(self):
        return self.nom