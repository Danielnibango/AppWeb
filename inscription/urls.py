from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home ,name='dashboard'),
    path('dashboard.htm', views.dash, name='dashboard'),
    
    # Formations
    path('formations/', views.liste_formations, name='liste_formations'),
    path('formations/<int:formation_id>/', views.detail_formation, name='detail_formation'),
    path('formations/<int:formation_id>/creer-demande/', views.creer_demande, name='creer_demande'),

    # Paiements
    path('paiements/', views.liste_paiements, name='liste_paiements'),

    # Cours
    path('liste/', views.liste_cours, name='liste'),

    # Notifications
    path('notifications/', views.liste_notifications, name='liste_notifications'),

    # Tableau de bord
    path('dashboard/', views.dashboard, name='dashboard'),
]