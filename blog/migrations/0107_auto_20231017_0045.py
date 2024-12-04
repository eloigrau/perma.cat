# Generated by Django 2.2.28 on 2023-10-16 22:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0106_documentpartage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentpartage',
            name='nom',
            field=models.CharField(default='', help_text='Minimum 6 lettres', max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Nom du document'),
        ),
    ]
