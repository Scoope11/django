from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from mainapp.forms import AuthForm, RegisterForm


def login(request):
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AuthForm()
    context = {
        'title' : 'Авторизация',
        'form' : form,
    }
    return render(request, 'mainapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = RegisterForm()
    context = {
        'title' : 'Регистрация',
        'form' : form,
    }
    return render(request, 'mainapp/register.html', context)


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))