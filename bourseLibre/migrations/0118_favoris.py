# Generated by Django 4.2.14 on 2024-12-17 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bourseLibre', '0117_messageadmin_sujet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoris',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('url', models.URLField(max_length=300)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Profil')),
            ],
        ),
    ]
