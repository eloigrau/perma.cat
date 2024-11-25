# -*- coding: utf-8 -*-
"""bourseLibre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog__ import urls as blog_urls
    2. Add a URL to urlpatterns:  re_path(r'^blog__/', include(blog_urls))
"""
from django.urls import path, include
from . import views, views_phoning
from django.contrib.auth.decorators import login_required

app_name = 'adherents'

urlpatterns = [
    path('conf66/', login_required(views.ListeAdherents.as_view()), name="accueil"),
    path('conf66/accueil_admin/', views.accueil_admin, name="accueil_admin"),
    path('conf66/get_csv_adherents/', views.get_csv_adherents, name="get_csv_adherents"),
    path('conf66/get_infos_adherents_pasajour/', views.get_infos_adherents_pasajour, name="get_infos_adherents_pasajour"),
    path('conf66/get_infos_adherents_ajour/', views.get_infos_adherents_ajour, name="get_infos_adherents_ajour"),
    path('conf66/get_csv_listeMails/', views.get_csv_listeMails, name="get_csv_listeMails"),
    path(r'conf66/infos_adherents/<str:type_info>', views.get_infos_adherent, name="get_infos_adherent"),
    path(r'conf66/infos_listeMail/<int:listeMail_pk>/<str:type_info>', views.get_infos_listeMail, name="get_infos_listeMail"),

    path('conf66/import_csv/', views.import_adherents_ggl, name="import_csv"),
    path('conf66/modif_APE/', views.modif_APE, name="modif_APE"),
    path('conf66/normaliser_adherents/', views.normaliser_adherents, name="normaliser_adherents"),

    path(r'conf66/adherents/', login_required(views.ListeAdherents.as_view()), name="adherent_liste"),
    path(r'conf66/adherent/ajouter/', views.adherent_ajouter, name="adherent_ajouter"),
    path(r'conf66/adherent/detail/<int:pk>', login_required(views.AdherentDetailView.as_view()), name="adherent_detail"),
    path(r'conf66/adherent/monProfil', views.monProfil, name="monProfil"),
    path(r'conf66/adherent/modifier/<int:pk>', login_required(views.AdherentUpdateView.as_view()), name="adherent_modifier"),
    path(r'conf66/adherent/adherents_modifier_adresse/<int:pk>', login_required(views.AdherentAdresseUpdateView.as_view()), name="adherents_modifier_adresse"),
    path(r'conf66/adherent/supprimer/<int:pk>', login_required(views.AdherentDeleteView.as_view()), name="adherent_supprimer"),

    path(r'conf66/adhesions/', login_required(views.ListeAdhesions.as_view()), name="adhesion_liste"),
    path(r'conf66/adhesion/creer/<int:adherent_pk>', views.ajouterAdhesion, name="adhesion_creer"),
    path(r'conf66/adhesion/creer/', views.ajouterAdhesion_2, name="adhesion_creer_adherent"),
    path(r'conf66/adhesion/detail/<int:pk>', login_required(views.AdhesionDetailView.as_view()), name="adhesion_detail"),
    path(r'conf66/adhesion/modifier/<int:pk>', login_required(views.AdhesionUpdateView.as_view()), name="adhesion_modifier"),
    path(r'conf66/adhesion/supprimer/<int:pk>', login_required(views.AdhesionDeleteView.as_view()), name="adhesion_supprimer"),

    path(r'conf66/inscriptions/listesInscriptions', login_required(views.ListeInscriptionsMails.as_view()), name="inscriptionMail_liste"),
    path(r'conf66/inscriptions/creer/<int:adherent_pk>', views.creerInscriptionMail_adherent, name="inscriptionMail_adherent"),
    path(r'conf66/inscriptions/creer/', views.creerInscriptionMail, name="inscriptionMail_creer"),
    path(r'conf66/inscriptions/detail/<int:pk>', login_required(views.InscriptionMailDetailView.as_view()), name="inscriptionMail_detail"),
    path(r'conf66/inscriptions/modifier/<int:pk>', login_required(views.InscriptionMailUpdateView.as_view()), name="inscriptionMail_modifier"),
    path(r'conf66/inscriptions/supprimer/<int:pk>', login_required(views.InscriptionMailDeleteView.as_view()), name="inscriptionMail_supprimer"),

    path(r'conf66/comm_adh/modifier/<int:pk>', login_required(views.Comm_adherent_modifier.as_view()), name="comm_adherent_modifier"),
    path(r'conf66/comm_adh/supprimer/<int:pk>', login_required(views.Comm_adherent_supprimer.as_view()), name="comm_adherent_supprimer"),
    path(r'conf66/comm_adh/creer/<int:adherent_pk>', views.ajouter_comm_adh, name="ajouter_comm_adh"),

    path(r'conf66/listesDiffusion/', login_required(views.ListeDiffusionConf_liste.as_view()), name="listeDiffusionConf_liste"),
    path(r'conf66/listesDiffusion/creerListe/', views.creerListeDiffusionConf, name="listeDiffusionConf_creer"),
    path(r'conf66/listesDiffusion/detail/<int:pk>', login_required(views.ListeDiffusionConfDetailView.as_view()), name="listeDiffusion_detail"),
    path(r'conf66/listesDiffusion/modifier/<int:pk>', login_required(views.ListeDiffusionConfUpdateView.as_view()), name="listeDiffusion_modifier"),
    path(r'conf66/listesDiffusion/supprimer/<int:pk>', login_required(views.ListeDiffusionConfDeleteView.as_view()), name="listeDiffusionsupprimer"),
    path(r'conf66/listesDiffusion/mesListesMails/', views.mesListesMails, name="mesListesMails"),
    path(r'conf66/inscriptions/swap_inscription/<int:listeMail_pk>/<int:adherent_pk>',
         views.swap_inscription, name="swap_inscription"),

    path(r'conf66/listesDiffusion/ajouter/<int:listeDiffusion_pk>/', views.ajouterAdherentAListeDiffusionConf,
         name="listeDiffusion_ajouterAdherent"),
    path(r'conf66/inscriptions/ajouter/<int:adherent_pk>',
         views.ajouterInscription_AdherentListeDiffusionConf, name="ajouterInscription_AdherentListeDiffusionConf"),


    path(r'conf66/phoning/complet', login_required(views_phoning.Paysan_liste.as_view()), name="accueil_phoning_complet"),
    path(r'conf66/phoning/simple', login_required(views_phoning.Paysan_liste.as_view()), name="accueil_phoning"),
    #path(r'conf66/phoning/paysan_ajouter/', views.creerListeDiffusionConf, name="listeDiffusionConf_creer"),
    path(r'conf66/phoning/ajouter/acceuil', views_phoning.paysan_ajouter_accueil, name="phoning_paysan_ajouter_accueil"),
    path(r'conf66/phoning/ajouter', login_required(views_phoning.Paysan_ajouter.as_view()),
         name="phoning_paysan_ajouter"),
    path(r'conf66/phoning/ajouter/listetel', views_phoning.phoning_paysan_ajouter_listetel,
         name="phoning_paysan_ajouter_listetel"),
    path(r'conf66/phoning/ajouter/csv', views_phoning.phoning_paysan_ajouter_csv, name="phoning_paysan_ajouter_csv"),
    path(r'conf66/phoning/ajouter/adhconf', views_phoning.ajouterAdherentsConf, name="phoning_ajouterAdherentsConf"),
    path(r'conf66/phoning/supprimer/doublons', views_phoning.supprimer_doublons, name="phoning_supprimer_doublons"),
    path(r'conf66/phoning/supprimer/nettoyer_telephones', views_phoning.nettoyer_telephones, name="nettoyer_telephones"),
    path(r'conf66/phoning/modifier/<int:pk>', login_required(views_phoning.Paysan_modifier.as_view()), name="phoning_paysan_modifier"),
    path(r'conf66/phoning/supprimer/<int:pk>', login_required(views_phoning.Paysan_supprimer.as_view()), name="phoning_paysan_supprimer"),
    path(r'conf66/phoning/supprimer2/<int:paysan_pk>', views_phoning.paysan_supprimer, name="phoning_paysan_supprimer2"),
    path(r'conf66/phoning/contact/ajouter/<int:paysan_pk>', views_phoning.contactPaysan_ajouter, name="phoning_paysan_contact_ajout"),
    path(r'conf66/phoning/contact/supprimer/<int:paysan_contact_pk>', views_phoning.contactPaysan_supprimer, name="phoning_paysan_contact_supprimer"),
    path(r'conf66/phoning/get_csv_paysans/', views_phoning.get_csv_paysans, name="get_csv_paysans")
]
