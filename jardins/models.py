from django.db import models
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from bourseLibre.models import Profil, Adresse
import uuid

class Choix():
    type_jardin =  ('0', 'Jardin Collectif - associatif'), ('1', 'Jardin Collectif - municipal'), ('2', 'Jardin Collectif - Privé'), ('3', 'Jardin Individuel - Privé')
    type_grainotheque = ('0', 'Grainothèque Collective - association'), ('2', 'Grainothèque Collective - médiathèque, école, ...'), ('3', 'Grainothèque Privée'),

    visibilite_jardin_annuaire = ('0', "Public (visible dans l'annuaire sans inscription)"), ('1', 'Inscrits (visible dans seulement par les inscrits au site)'), ('2', "Invisible dans l'annuaire")
    visibilite_jardin_adresse = ('0', 'Adresse visible sans inscription'), ('1', 'Adresse visible seulement par les inscrits'), ('2', 'Adresse invisible (carte)')

class DBRang_inpn(models.Model):
    RG_LEVEL = models.IntegerField()
    RANG = models.CharField(max_length=5)
    DETAIL = models.CharField(max_length=30)
    DETAIL_EN = models.CharField(max_length=30)

    def __str__(self):
        return str(self.DETAIL)

class DBStatut_inpn(models.Model):
    ORDRE = models.CharField(max_length=4)
    STATUT = models.CharField(max_length=2)
    DESCRIPTION = models.CharField(max_length=150)
    DEFINITION = models.TextField(null=True)

    def __str__(self):
        return self.DESCRIPTION + " (" + self.DEFINITION + ")"

class DBHabitat_inpn(models.Model):
    HABITAT = models.IntegerField()
    LB_HABITAT = models.TextField(null=True)
    DEFINITION = models.TextField(null=True)

    def __str__(self):
        return self.LB_HABITAT + " (" + self.DEFINITION + ")"

class DBVern_inpn(models.Model):
    CD_VERN = models.IntegerField(unique=True)
    CD_NOM = models.IntegerField()
    LB_VERN = models.TextField(null=True, blank=True)
    NOM_VERN_SOURCE = models.CharField(max_length=400)
    LANGUE = models.CharField(max_length=400)
    ISO639_3 = models.CharField(max_length=400)
    PAYS = models.CharField(max_length=400)

    def __str__(self):
        return str(self.LB_VERN)


class DB_importeur(models.Model):
    nom = models.CharField(max_length=15)
    texte = models.TextField(blank=True, null=True, )
    lg_debut = models.IntegerField(default=0)
    lg_fin = models.IntegerField(default=0)

    def __str__(self):
        return str(self.lg_debut) + " fin " + str(self.lg_fin)


class Plante(models.Model):
    REGNE = models.CharField(max_length=15)
    PHYLUM = models.CharField(max_length=30)
    CLASSE = models.CharField(max_length=50)
    ORDRE = models.CharField(max_length=50)
    FAMILLE = models.CharField(max_length=50)
    SOUS_FAMILLE = models.CharField(max_length=50)
    TRIBU = models.CharField(max_length=50)
    GROUP1_INPN = models.CharField(max_length=20)
    GROUP2_INPN = models.CharField(max_length=20)
    GROUP3_INPN = models.CharField(max_length=20)
    CD_NOM = models.IntegerField(unique=True, primary_key=True)
    CD_TAXSUP = models.CharField(max_length=8)
    CD_SUP = models.CharField(max_length=8)
    CD_REF = models.IntegerField()
    RANG = models.CharField(max_length=4)
    LB_NOM = models.CharField(max_length=200) #Nom scientifique
    LB_AUTEUR = models.CharField(max_length=200, null=True)
    NOM_COMPLET = models.TextField(null=True)
    NOM_COMPLET_HTML = models.TextField(null=True)
    NOM_VALIDE = models.CharField(max_length=250)
    NOM_VERN = models.CharField(max_length=350)
    NOM_VERN_ENG = models.CharField(max_length=250)
    HABITAT = models.CharField(max_length=40)
    FR = models.CharField(max_length=2)
    GF = models.CharField(max_length=2)
    MAR = models.CharField(max_length=2)
    GUA = models.CharField(max_length=2)
    SM = models.CharField(max_length=2)
    SB = models.CharField(max_length=2)
    SPM = models.CharField(max_length=2)
    MAY = models.CharField(max_length=2)
    EPA = models.CharField(max_length=2)
    REU = models.CharField(max_length=2)
    SA = models.CharField(max_length=2)
    TA = models.CharField(max_length=2)
    TAAF = models.CharField(max_length=2)
    PF = models.CharField(max_length=2)
    NC = models.CharField(max_length=2)
    WF = models.CharField(max_length=2)
    CLI = models.CharField(max_length=2)
    URL = models.CharField(max_length=200)
    infos_supp = models.TextField(null=True)


    def __str__(self):
        return self.NOM_VERN

    @property
    def get_nom_espece(self):
        return self.NOM_VERN + ", " + self.LB_NOM

    @property
    def get_inpi_url(self):
        return self.URL

    @property
    def get_habitat(self):
        return DBHabitat_inpn.objects.get(HABITAT=self.HABITAT)

    @property
    def get_rang(self):
        return str(DBRang_inpn.objects.get(RANG=self.RANG))

    @property
    def get_nomvern(self):
        try:
            return DBVern_inpn.objects.get(CD_NOM=self.CD_NOM)
        except:
            return ""

    @property
    def get_absolute_url(self):
        return reverse('jardins:voir_plante', kwargs={'cd_nom':self.CD_NOM})

    @property
    def get_info_supp_html(self):
        return "; ".join([" <a href='"+str(x)+"' target='_blank'>"+str(i)+"</a>" for i, x in enumerate(self.infos_supp.split('; '))])


    @property
    def has_info_supp(self):
        return len(self.infos_supp.split('; ')) > 2

    @property
    def get_info_supp_html2(self):
        if not self.infos_supp:
            return
        return [str(x) for x in self.infos_supp.split('; ') if x]


class Plante_recherche(models.Model):
    plante = models.ForeignKey(Plante, on_delete=models.CASCADE)

class Jardin(models.Model):
    auteur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="auteur_jardin")
    referent = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="referent_jardin", blank=True, null=True)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE, blank=True, null=True)
    categorie = models.CharField(max_length=3,
        choices=Choix.type_jardin,
        default='', verbose_name="Type de jardin*")
    visibilite_annuaire = models.CharField(max_length=3,
        choices=Choix.visibilite_jardin_annuaire,
        default='', verbose_name="Visibilité du jardin sur l'annuaire")
    visibilite_adresse = models.CharField(max_length=30,
        choices=Choix.visibilite_jardin_adresse,
        default='', verbose_name="Visibilité de l'adresse du jardin (sur la carte)")
    titre = models.CharField(max_length=250, verbose_name="Nom du jardin*")
    date_creation = models.DateTimeField(verbose_name="Date de création", default=timezone.now)
    slug = models.SlugField(max_length=100)
    description = models.TextField(null=True, blank=True, help_text="Décrivez le jardin en quelques mots")
    fonctionnement = models.TextField(null=True, blank=True, help_text="Un descriptif du fonctionnement du jardin (horaires, participation, gestion de l'eau, ...)")
    permapotes_id = models.CharField(max_length=250, verbose_name="Identifiants sur permapotes.com", null=True, )
    horaires = models.TextField(null=True, help_text="Horaires d'ouverture (s'il y a lieu)")
    parcellesIndividuelles = models.BooleanField(default=False, verbose_name="Parcelles Individuelles")
    parcellesCollectives = models.BooleanField(default=False, verbose_name="Parcelles Collectives")
    email_contact = models.EmailField( verbose_name="Email de contact*")
    telephone = models.CharField(max_length=15, blank=True, verbose_name="Numéro de telephone de contact")

    def get_absolute_url(self):
        return reverse('jardins:jardin_lire', kwargs={'slug':self.slug})

    def __str__(self):
        return self.titre

    def get_visibilite_display(self):
        return str(self.get_visibilite_annuaire_display()) + " / "+ str(self.get_visibilite_adresse_display())

class Grainotheque(models.Model):
    categorie = models.CharField(max_length=3,
        choices=Choix.type_grainotheque,
        default='', verbose_name="Type de grainotheque*")
    auteur = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="auteur_grainotheque")
    referent = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="referent_grainotheque", blank=True, null=True)
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE, blank=True, null=True)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE, blank=True, null=True)
    date_creation = models.DateTimeField(verbose_name="Date de création", default=timezone.now)
    email_contact = models.EmailField( verbose_name="Email de contact*")

    visibilite_annuaire = models.CharField(max_length=30,
        choices= Choix.visibilite_jardin_annuaire,
        default='', verbose_name="Visibilité de la grainothèque sur l'annuaire")
    visibilite_adresse = models.CharField(max_length=30,
        choices= Choix.visibilite_jardin_adresse,
        default='', verbose_name="Visibilité de l'adresse de la grainotheque (sur la carte)")
    titre = models.CharField(max_length=250,)
    slug = models.SlugField(max_length=100)

    description = models.TextField(null=True)


    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('jardins:grainotheque_lire', kwargs={'slug':self.slug})

    def get_visibilite_display(self):
        return str(self.get_visibilite_annuaire_display()) + " "+ str(self.get_visibilite_adresse_display())

class InfoGraine(models.Model):
    date_recolte = models.DateTimeField(verbose_name="Date de récolte", default=timezone.now)
    duree_germinative = models.FloatField(verbose_name="Durée de conservation (années)", blank=True, default="5")
    stock_quantite = models.CharField(max_length=120, blank=True, verbose_name="Quantité de graines (nombre ou grammes)",)
    description = models.TextField(null=True, blank=True, help_text="Description (infos supplémentaires")

    def __str__(self):
        return str(self.description) + " " + str(self.stock_quantite) + " "+ str(self.duree_germinative)+ " "+ str(self.date_recolte)

    def get_edit_url(self):
        return reverse('jardins:grainotheque_editInfosGraine', kwargs={'pk':self.pk})

    def get_absolute_url(self):
        return reverse('jardins:grainotheque_lire', kwargs={'slug':self.graine.grainotheque.slug})

class Graine(models.Model):
    grainotheque = models.ForeignKey(Grainotheque, on_delete=models.CASCADE,)
    plante = models.ForeignKey(Plante, on_delete=models.CASCADE)
    infos = models.OneToOneField(InfoGraine, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.plante) + " " + str(self.infos)

    def get_absolute_url(self):
        return reverse('jardins:grainotheque_lire', kwargs={'slug':self.grainotheque.slug})

    @property
    def get_str_html_header(self):
        return "<thead><tr><th> Plante</th><th>Description</th><th>Stock</th><th>Durée germinative</th><th>Date de récolte</th></tr></thead>"

    @property
    def get_str_html(self):
        return "<tr><td><a href='"+self.plante.get_absolute_url()+"'>"+str(self.plante) +"</a></td><td>" + str(self.infos.description) +"</td><td>" + str(self.infos.stock_quantite) + "</td><td>" + str(self.infos.duree_germinative) + "</td><td>" + str(self.infos.date_recolte.strftime('%d/%m/%Y')) +"</td></tr>"

class InscriptionJardin(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="jardin_suiveur")
    jardin = models.ForeignKey(Jardin, on_delete=models.CASCADE, related_name="jardin_suivi")
    date_inscription = models.DateTimeField(verbose_name="Date d'inscription", editable=False, auto_now_add=True)

    def __unicode__(self):
        return self.__str()

    def __str__(self):
        return "(" + str(self.id) + ") " + str(self.user) + " " + str(self.date_inscription) + " " + str(
            self.jardin)

class InscriptionGrainotheque(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="grainotheque_suiveur")
    grainotek = models.ForeignKey(Grainotheque, on_delete=models.CASCADE, related_name="grainotheque_suivi" )
    date_inscription = models.DateTimeField(verbose_name="Date d'inscription", editable=False, auto_now_add=True)

    def __str__(self):
        return "(" + str(self.id) + ") " + str(self.user) + " " + str(self.date_inscription) + " " + str(
            self.jardin)

class GenericModel(models.Model):
    type_article = models.CharField(max_length=100)
    message = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.__str()

    def __str__(self):
        return self.type_article

    def get_absolute_url(self):
        return reverse("jardins:accueil")