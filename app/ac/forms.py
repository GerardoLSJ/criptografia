from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CustomAuthenticationForm(AuthenticationForm):
  username = forms.CharField(label='Nombre de usuario', widget=TextInput(attrs={'class': 'form-control','placeholder': 'Usuario'}))
  password = forms.CharField(label='Contraseña', widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Constraseña'}))

class SignForm(forms.Form):
  fileName = forms.CharField(label='Nombre del archivo a firmar',  
                              max_length=100,
                              widget=TextInput(
                                attrs={'class': 'form-control','placeholder':'Nombre del archivo a firmar'}
                              )
  )
  fistName = forms.CharField(label='Nombre(s)',  
                              max_length=100,
                              widget=TextInput(
                                attrs={'class': 'form-control','placeholder':'Nombre(s)','readonly':'readonly'}
                              )
  )

  lastName = forms.CharField(label='Apellido(s)',  
                              max_length=100,
                              widget=TextInput(
                                attrs={'class': 'form-control','placeholder':'Apellido(s)','readonly':'readonly'}
                              )
  )

  username = forms.CharField(label='Nombre de usuario',  
                              max_length=100,
                              widget=TextInput(
                                attrs={'class': 'form-control','placeholder':'Nombre de usuario', 'readonly':'readonly'}
                              )
  )
  serverLocation = forms.CharField(label='Ubicación del servidor',  
                              max_length=100,
                              widget=TextInput(
                                attrs={'class': 'form-control','placeholder':'Ubicación del servidor', 'readonly':'readonly'}
                              )
  )


