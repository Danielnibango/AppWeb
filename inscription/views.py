
from django.shortcuts import render, get_object_or_404, redirect
from .models import Utilisateur, Formation, Demande, Paiement, Cours, Notification, Module


def home(request):

    return render(request, "dashboard.html")

def dash(request):
    return render(request, 'dashboard.html')


# Vue pour afficher la liste des formations
def liste_formations(request):
    formations = Formation.objects.all()
    return render(request, 'formations/liste.html', {'formations': formations})

# Vue pour afficher les détails d'une formation
def detail_formation(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    return render(request, 'formations/detail.html', {'formation': formation})

# Vue pour créer une demande de formation
def creer_demande(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    if request.method == 'POST':
        lettre = request.POST.get('lettre')
        candidat = request.user.utilisateur  # Supposons que l'utilisateur est connecté
        Demande.objects.create(candidat=candidat, formation=formation, lettre=lettre, status='En attente')
        return redirect('liste_formations')
    return render(request, 'demandes/creer.html', {'formation': formation})

# Vue pour afficher les paiements d'un utilisateur
def liste_paiements(request):
    paiements = Paiement.objects.filter(demande__candidat=request.user.utilisateur)
    return render(request, 'paiements/liste.html', {'paiements': paiements})

# Vue pour afficher la liste des cours
def liste_cours(request):
    # cours = Cours.objects.all()
    cours = Cours.objects.select_related('module').all()
    
    return render(request, 'cours/liste.html', {'cours': cours, 'cours': cours})

# Vue pour afficher les notifications d'un utilisateur
def liste_notifications(request):
    notifications = Notification.objects.filter(utilisateur=request.user.utilisateur)
    return render(request, 'notifications/liste.html', {'notifications': notifications})

# Vue pour le tableau de bord de l'utilisateur
def dashboard(request):
    utilisateur = request.user.utilisateur
    demandes = Demande.objects.filter(candidat=utilisateur)
    paiements = Paiement.objects.filter(demande__candidat=utilisateur)
    notifications = Notification.objects.filter(utilisateur=utilisateur)
    return render(request, 'dashboard.html', {
        'demandes': demandes,
        'paiements': paiements,
        'notifications': notifications,
    })
