# Generated by Django 2.2.28 on 2023-09-09 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jardins', '0058_auto_20230909_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoplante',
            old_name='type_vegetation',
            new_name='type_plante',
        ),
    ]
