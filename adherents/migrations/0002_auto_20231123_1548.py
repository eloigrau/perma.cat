# Generated by Django 2.2.28 on 2023-11-23 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adherents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adherent',
            old_name='mail',
            new_name='email',
        ),
    ]
