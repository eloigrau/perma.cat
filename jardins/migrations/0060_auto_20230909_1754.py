# Generated by Django 2.2.28 on 2023-09-09 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jardins', '0059_auto_20230909_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantedejardin',
            name='jardin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plantedejardin_jardin', to='jardins.Jardin'),
        ),
    ]
