from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('modifier/<int:pk>/', views.modifier_produit, name='modifier_produit'),
    path('supprimer/<int:pk>/', views.supprimer_produit, name='supprimer_produit'),
  path('home/', views.home, name='home'),
  path('login/', views.login_view, name='login'),
  path('vente/', views.vente, name='vente'), 
  path('statistiques/', views.statistiques, name='statistiques'), 
path('signup/', views.signup_view, name='signup'),
path('logout/', views.logout_view, name='logout'),



]
