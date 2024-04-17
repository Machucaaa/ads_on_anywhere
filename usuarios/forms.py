from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Propietario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Propietario
        fields = "__all__"

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'nombre de usuario?'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'email?'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'password?'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'confirmar password'}))
    class Meta:
        model = Propietario
        fields = ['username', 'email', 'password1', 'password2']       