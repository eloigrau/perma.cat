# Generated by Django 2.2.28 on 2023-09-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ateliers', '0035_auto_20230825_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atelier',
            name='categorie',
            field=models.CharField(choices=[('0', 'Permaculture'), ('1', 'Bricolage'), ('2', 'Cuisine'), ('3', 'Bien-être'), ('4', 'Musique'), ('6', 'Politique'), ('8', 'Culture'), ('7', 'Activité Pro'), ('9', 'Informatique'), ('5', 'Autre...')], default='0', max_length=30, verbose_name='categorie'),
        ),
    ]
