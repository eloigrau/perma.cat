# Generated by Django 2.2.28 on 2023-10-25 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bourseLibre', '0107_salon_tags'),
        ('blog', '0109_associationsalonarticle'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='associationsalonarticle',
            unique_together={('article', 'salon')},
        ),
    ]
