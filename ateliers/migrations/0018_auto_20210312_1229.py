# Generated by Django 2.2.13 on 2021-03-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ateliers', '0017_atelier_asso'),
    ]

    operations = [
#        migrations.RemoveField(
#            model_name='atelier',
#            name='outils',
#        ),
#         migrations.AlterField(
#             model_name='atelier',
#             name='heure_atelier',
#             field=models.TimeField(blank=True, default='17:00', help_text='Horaire de départ (hh:mm)', null=True, verbose_name='Heure prévue'),
#         ),
        migrations.AlterField(
            model_name='atelier',
            name='materiel',
            field=models.TextField(blank=True, null=True, verbose_name='Matériel/outils nécessaires'),
        ),
    ]
