# Generated by Django 4.2.14 on 2024-07-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardins', '0065_remove_plantedejardin_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoplante',
            name='comestibilite',
            field=models.CharField(choices=[('0', 'Comestibilité inconnue'), ('1', 'Non comestible'), ('2', 'Comestible (tout)'), ('3', 'Comestible (feuilles)'), ('4', 'Comestible (fruit)'), ('5', 'Comestible (fleur)'), ('6', 'Comestible (racines)')], default='0', max_length=3, verbose_name='Comestibilité'),
        ),
    ]
