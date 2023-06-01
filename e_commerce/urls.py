from django.urls import path

from . import views

app_name = "e_commerce"
urlpatterns = [
    path("", views.index, name="index"),
    path("connexion/", views.connexion, name="connexion"),
    path("inscription/", views.inscription, name="inscription"),
    path("panier/", views.panier, name="panier"),
]
