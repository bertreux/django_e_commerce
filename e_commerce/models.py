from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        # Crée un utilisateur avec l'e-mail et le mot de passe fournis
        # Vous pouvez également ajouter d'autres champs personnalisés ici
        if not email:
            raise ValueError('L\'adresse e-mail est obligatoire')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # Ajoutez d'autres champs personnalisés si nécessaire

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Produit(models.Model):
    contenu = models.CharField(max_length=200)
    prix = models.IntegerField(default=0)
    titre = models.CharField(max_length=100)

class Panier(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
