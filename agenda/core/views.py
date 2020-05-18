from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from core.models import Evento

# Create your views here.

#def index(request):
#   return redirect('/agenda/')

def entrar(request):

    if request.POST:
        username = request.POST.get("user")
        password = request.POST.get("password")
        accept = authenticate(username=username, password=password)
        if accept is not None:
            login(request, accept)
            return redirect("/")
        else:
            messages.error(request, "Invalid user or password!")
            
    return redirect("/")

def login_user(request):
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/login/")
def lista_eventos(request):

    username = request.user
    evento = Evento.objects.filter(usuario=username)
    data = {"eventos":evento}
    return render(request, "agenda.html", data)
