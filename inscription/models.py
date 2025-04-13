;from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    id_ut = models.AutoField(primary_key=True)  # Identifiant unique
    nom = models.CharField(max_length=100)  # Nom de l'utilisateur
    email = models.EmailField(unique=True)  # Email unique
    mot_de_passe = models.CharField(max_length=100)  # Mot de passe

    # Ajoutez des related_name uniques pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="utilisateur_groups",  # Nom unique pour la relation inverse
        related_query_name="utilisateur",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="utilisateur_permissions",  # Nom unique pour la relation inverse
        related_query_name="utilisateur",
    )

    def __str__(self):
        return self.nom
    
    
class Admin(Utilisateur):
    id_ad = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Admin: {self.nom}"
    
    
# Modèle Conducteur
class Conducteur(models.Model):
    id_can = models.AutoField(primary_key=True)  # Identifiant unique
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)  # Relation avec Utilisateur
    adresse = models.CharField(max_length=200)  # Adresse du conducteur
    telephone = models.CharField(max_length=20)  # Téléphone du conducteur
    age = models.IntegerField()  # Âge du conducteur
    sexe = models.CharField(max_length=10)  # Sexe du conducteur

    def __str__(self):
        return f"Conducteur: {self.utilisateur.nom}"


# Modèle Formateur
class Formateur(models.Model):
    id_form = models.AutoField(primary_key=True)  # Identifiant unique
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)  # Relation avec Utilisateur

    def __str__(self):
        return f"Formateur: {self.utilisateur.nom}"


# Modèle Formation
class Formation(models.Model):
    id_for = models.AutoField(primary_key=True)  # Identifiant unique
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)  # Relation avec Formateur
    date_debut = models.DateField()  # Date de début de la formation
    date_fin = models.DateField()  # Date de fin de la formation

    def __str__(self):
        return f"Formation {self.id_for} par {self.formateur.utilisateur.nom}"


# Modèle Demande
class Demande(models.Model):
    id = models.AutoField(primary_key=True)  # Identifiant unique
    candidat = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)  # Relation avec Utilisateur
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)  # Relation avec Formation
    lettre = models.TextField()  # Lettre de motivation
    status = models.CharField(max_length=50)  # Statut de la demande

    def __str__(self):
        return f"Demande {self.id} par {self.candidat.nom}"


# Modèle Paiement
class Paiement(models.Model):
    id = models.AutoField(primary_key=True)  # Identifiant unique
    demande = models.ForeignKey(Demande, on_delete=models.CASCADE)  # Relation avec Demande
    mode_pay = models.CharField(max_length=50)  # Mode de paiement
    montant = models.DecimalField(max_digits=10, decimal_places=2)  # Montant du paiement
    date = models.DateField()  # Date du paiement

    def __str__(self):
        return f"Paiement {self.id} pour {self.demande.id}"

class Module(models.Model):
    nom = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nom

class Cours(models.Model):
    id_cou = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=200)
    contenu = models.TextField()
    frais = models.DecimalField(max_digits=10, decimal_places=2)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='cours', null=True, blank=True)

    def __str__(self):
        return self.intitule



# Modèle Notification
class Notification(models.Model):
    id = models.AutoField(primary_key=True)  # Identifiant  unique
    titre = models.CharField(max_length=100)  # Titre de la notification
    description = models.TextField()  # Description de la notification
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)  # Relation avec Utilisateur

    def __str__(self):
        return f"Notification {self.titre} pour {self.utilisateur.nom}"