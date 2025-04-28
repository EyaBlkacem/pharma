from django.shortcuts import render

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


def home(request):
    return render(request, 'pharma_app/home.html')

def login_view(request):
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
