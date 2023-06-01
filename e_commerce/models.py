from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User

class Produit(models.Model):
    contenu = models.CharField(max_length=200)
    prix = models.IntegerField(default=0)
    titre = models.CharField(max_length=100)

class Panier(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
