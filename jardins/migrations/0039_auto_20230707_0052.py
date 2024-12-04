# Generated by Django 2.2.28 on 2023-07-06 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardins', '0038_auto_20230706_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grainotheque',
            name='categorie',
            field=models.CharField(choices=[('0', 'Grainothèque Collective - association'), ('2', 'Grainothèque Collective - médiathèque, école, ...'), ('3', 'Grainothèque Privée')], default='', max_length=3, verbose_name='Type de grainotheque*'),
        ),
        migrations.AlterField(
            model_name='jardin',
            name='categorie',
            field=models.CharField(choices=[('0', 'Jardin Collectif - associatif'), ('1', 'Jardin Collectif - municipal'), ('2', 'Jardin Collectif - Privé'), ('3', 'Jardin Individuel - Privé')], default='', max_length=3, verbose_name='Type de jardin*'),
        ),
    ]
