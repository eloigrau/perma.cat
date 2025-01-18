# Generated by Django 4.2.14 on 2025-01-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adherents', '0035_contactcontact_profil_alter_contactcontact_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactcontact',
            name='statut',
            field=models.CharField(choices=[('', '--------'), ('0', 'Réponse OK'), ('1', 'Pas de réponse'), ('2', 'A répondu mais à rappeler'), ('3', 'A répondu mais HOSTILE'), ('4', 'Mauvais numéro'), ('6', 'autre: '), ('5', "Je l'appellerai")], default='', max_length=2, verbose_name='Statut'),
        ),
    ]
