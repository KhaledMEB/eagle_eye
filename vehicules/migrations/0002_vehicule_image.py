# Generated by Django 3.0.3 on 2020-06-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='vehicules_pics'),
        ),
    ]