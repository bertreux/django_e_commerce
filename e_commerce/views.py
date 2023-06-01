from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Panier, Produit, User

def index(request):
    data = Produit.objects.all()
    produit = {'produit': data}
    return render(request, "e_commerce/index.html", produit)
def connexion(request):
    print(request)
    if request.method == 'POST':
        email = request.POST['mail']
        password = request.POST['pwd']
        user = authenticate(request, mail=email, pwd=password)
        if user is not None:
            login(request, user)
            data = Produit.objects.all()
            produit = {'produit': data}
            return render(request, "e_commerce/index.html", produit)
        else:
            error_message = 'Identifiants invalides'
            return render(request, "e_commerce/connexion.html", {'error_message': error_message})
    else:
        return render(request, "e_commerce/connexion.html")

def inscription(request):
    return render(request, "e_commerce/inscription.html")

def panier(request):
    return render(request, "e_commerce/panier.html")
