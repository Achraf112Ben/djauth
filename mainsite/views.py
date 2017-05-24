from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout

from .models import LoginForm


def index(request):
    context = {}
    if request.user.is_authenticated:
    	return render(request, 'mainsite/index2.html', context)
    else: 
    	return render(request, 'mainsite/index1.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'mainsite/login.html', {'form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))