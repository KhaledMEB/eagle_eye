# Generated by Django 3.0.7 on 2020-07-07 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendrier', '0007_auto_20200707_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='etat',
        ),
    ]
