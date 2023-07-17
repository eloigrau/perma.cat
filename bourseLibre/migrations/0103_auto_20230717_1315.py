# Generated by Django 2.2.28 on 2023-07-17 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bourseLibre', '0102_salon_jardin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscriptionnewslettergenerique',
            old_name='nom',
            new_name='nom_newsletter',
        ),
        migrations.AddField(
            model_name='inscriptionnewslettergenerique',
            name='profil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profil_newsletter', to=settings.AUTH_USER_MODEL, verbose_name='Profil du membre (si inscrit)'),
        ),
        migrations.CreateModel(
            name='Profil_recherche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
