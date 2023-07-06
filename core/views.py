from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def logout_user(request):
    logout(request)
    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
            return redirect('/')
    else:
        redirect('/')


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        dataEvento = request.POST.get('dataEvento')  # Obtém a data como uma string do formulário
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo, dataEvento=dataEvento, descricao=descricao, usuario=usuario)

    return redirect('/')


@login_required(login_url='/login/')
def listaEventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    response = {'eventos': evento}
    return render(request, 'agenda.html', response)


def index(request):
    return redirect('/agenda/')
