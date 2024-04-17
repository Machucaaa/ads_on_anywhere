from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from usuarios.models import Propietario
from usuarios.forms import CustomUserForm


def register(request): 
    form = CustomUserForm
    if request.method =='POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/para_editar_catalogo')
    context = {'form' : form }
    return render(request,'usuarios/auth/register.html', context )

def loginpage(request):
    if request.method=="POST":
        name = request.POST.get('username')
        passwd = request.POST.get('password')       
        user = authenticate(request, username=name, password=passwd)
        if user is not None:
            login(request, user) 
            return redirect('altascategoria')
        else:
            messages.error(request, 'Nombre de usuario o password no validos!')
            return redirect('/para_editar_catalogo')
        
    return render( request, 'usuarios/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/para_editar_catalogo')
    return redirect('/para_editar_catalogo')
