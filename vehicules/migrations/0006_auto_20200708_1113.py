# Generated by Django 3.0.3 on 2020-07-08 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicules', '0005_auto_20200708_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='statut',
            field=models.CharField(choices=[('AC', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='type',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Statut',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
