from django.contrib import admin
from .models import Utilisateur, Admin, Conducteur, Formateur, Formation, Demande, Paiement, Cours, Notification, Module

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id_ut', 'nom', 'email')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id_ad', 'nom')

@admin.register(Conducteur)
class ConducteurAdmin(admin.ModelAdmin):
    list_display = ('id_can', 'utilisateur', 'adresse', 'telephone')

@admin.register(Formateur)
class FormateurAdmin(admin.ModelAdmin):
    list_display = ('id_form', 'utilisateur')

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('id_for', 'formateur', 'date_debut', 'date_fin')

@admin.register(Demande)
class DemandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'candidat', 'formation', 'status')

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('id', 'demande', 'mode_pay', 'montant', 'date')

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('id_cou', 'intitule','module', 'frais')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'titre', 'utilisateur')
    
@admin.register(Module)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    
     
    
#     => Vérifie les fichiers modifiés : Avant d'ajouter les fichiers, tu peux voir quels fichiers ont été modifiés avec :
# git status 
# => Ajoute tous les fichiers modifiés : Utilise la commande suivante pour ajouter tous les fichiers modifiés :
# git add .
# => Commit les changements : Ensuite, tu peux valider les modifications avec :
# git commit -m "Modification des fichiers"
# => Pousser les modifications vers GitHub : Après avoir effectué le commit, tu peux envoyer tes changements vers GitHub avec :
# git push origin main
# Cela mettra à jour ton dépôt GitHub avec les modifications que tu as effectuées localement .