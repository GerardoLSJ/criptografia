from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CustomAuthenticationForm(AuthenticationForm):
  username = forms.CharField(label='Nombre de usuario', widget=TextInput(attrs={'class': 'form-control','placeholder': 'Usuario'}))
  password = forms.CharField(label='Contraseña', widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Constraseña'}))