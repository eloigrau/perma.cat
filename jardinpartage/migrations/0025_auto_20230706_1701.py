# Generated by Django 2.2.28 on 2023-07-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardinpartage', '0024_auto_20230706_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='jardin',
            field=models.CharField(choices=[('0', 'Tous les jardins'), ('1', 'Jardi Per Tots'), ('2', 'Jardin de Palau'), ('3', 'Jardins de Lurçat'), ('4', 'Gardiens de la Terre'), ('5', 'Fermille'), ('6', 'PPDM')], default='0', max_length=30, verbose_name='Jardin'),
        ),
    ]
