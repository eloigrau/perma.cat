# Generated by Django 4.2.14 on 2024-11-23 00:20

from django.db import migrations, models
import django.db.models.deletion



def copierListesDiffusion(apps, schema_migration):
    Listes_old = apps.get_model('adherents', 'ListeDiffusionConf')
    Listes_new = apps.get_model('adherents', 'ListeDiffusion')
    InscriptionMail_old = apps.get_model('adherents', 'InscriptionMail')
    InscriptionMail_new = apps.get_model('adherents', 'InscriptionMail_new')
    Assos = apps.get_model('bourseLibre', 'Asso')
    asso_conf = Assos.objects.get(abreviation="conf66")
    for l in Listes_old.objects.all():
        liste_new = Listes_new.objects.create(nom=l.nom, asso=asso_conf, date_creation=l.date_creation)
        for i in InscriptionMail_old.objects.filter(liste_diffusion=l):
            InscriptionMail_new.objects.create(liste_diffusion=liste_new, date_inscription=i.date_inscription,
                                               adherent=i.adherent, commentaire=i.commentaire)

    Adhesions = apps.get_model('adherents', 'Adhesion')
    Adherents = apps.get_model('adherents', 'Adherent')
    Listes = apps.get_model('adherents', 'listediffusionconf')

    for a in Adhesions.objects.all():
        a.asso = asso_conf
        a.save(update_fields=["asso", ])

    for a in Adherents.objects.all():
        a.asso = asso_conf
        a.save(update_fields=["asso", ])

    for a in Listes.objects.all():
        a.asso = asso_conf
        a.save(update_fields=["asso", ])

    Projets = apps.get_model('adherents', 'ProjetPhoning')
    projet_conf = Projets.objects.create(titre="EP CA 2024", asso=asso_conf)

    Contacts = apps.get_model('adherents', 'Contact')

    for a in Contacts.objects.all():
        a.projet = projet_conf
        a.save(update_fields=["projet", ])



class Migration(migrations.Migration):

    dependencies = [
        ('bourseLibre', '0115_alter_adresse_pays'),
        ('adherents', '0024_projetphoning'),
    ]

    operations = [
        migrations.AddField(
            model_name='adherent',
            name='asso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bourseLibre.asso', verbose_name='Groupe'),
        ),
        migrations.AddField(
            model_name='adhesion',
            name='asso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bourseLibre.asso'),
        ),
        migrations.AddField(
            model_name='listediffusionconf',
            name='asso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bourseLibre.asso', verbose_name='Groupe associé'),
        ),
        migrations.AddField(
            model_name='paysan',
            name='projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adherents.projetphoning', verbose_name='Groupe associé'),
        ),
        migrations.CreateModel(
            name='ListeDiffusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, unique=True)),
                ('date_creation', models.DateTimeField(auto_now=True, verbose_name='Date de création')),
                ('asso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bourseLibre.asso', verbose_name='Groupe associé')),
            ],
        ),
        migrations.CreateModel(
            name='InscriptionMail_new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_inscription', models.DateTimeField(auto_now_add=True, verbose_name="Date d'inscription")),
                ('commentaire', models.CharField(blank=True, max_length=50)),
                ('adherent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adherents.adherent', verbose_name='Adhérent')),
                ('liste_diffusion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adherents.listediffusion', verbose_name='Liste de diffusion')),
            ],
        ),
        migrations.RunPython(copierListesDiffusion)
    ]
