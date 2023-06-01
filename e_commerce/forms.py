from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-2'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-2'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3 mt-2'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-2'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3 mt-2'}), label='Confirmer le mot de passe')
