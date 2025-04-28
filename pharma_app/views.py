from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitForm

def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'pharma_app/liste_produits.html', {'produits': produits})
def vente(request):
    return render(request, 'pharma_app/vente.html')

def statistiques(request):
    return render(request, 'pharma_app/statistiques.html')



def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'pharma_app/signup.html', {'error': "Ce nom d'utilisateur existe déjà."})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'pharma_app/signup.html')

def home(request):
    return render(request, 'pharma_app/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige vers l'accueil après login
        else:
            return render(request, 'pharma_app/login.html', {'error': "Nom d'utilisateur ou mot de passe incorrect."})
    return render(request, 'pharma_app/login.html')

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'pharma_app/ajouter_produit.html', {'form': form})

def modifier_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'pharma_app/modifier_produit.html', {'form': form})

def supprimer_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'pharma_app/supprimer_produit.html', {'produit': produit})
