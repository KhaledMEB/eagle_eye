import json
from vehicules.models import Vehicule

with open('vehicules/vehicules.json') as f:
    veh_json = json.load(f)
for veh in veh_json:
    vehicule = Vehicule(nom=veh['nom'],
        vip=veh['vip'],
        matricule=veh['matricule'],
        statut=veh['statut'],
        type_v=veh['type_v'],
        groupe=veh['groupe'],
        compteur=veh['compteur'],
        conducteur=veh['conducteur'])
    vehicule.save()