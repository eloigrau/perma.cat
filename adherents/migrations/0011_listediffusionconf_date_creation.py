# Generated by Django 2.2.28 on 2023-12-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adherents', '0010_inscriptionmail_listediffusionconf'),
    ]

    operations = [
        migrations.AddField(
            model_name='listediffusionconf',
            name='date_creation',
            field=models.DateTimeField(auto_now=True, verbose_name='Date de creétion'),
        ),
    ]
