from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import (
    login, logout, authenticate
)
from django.contrib import messages
from .models import Home
import datetime as dt
from django.contrib.auth.models import User

@login_required
def home(request):
    template = loader.get_template("main/home.html")
    restos = Home.objects.all()
    context = {
        'restoslist' : restos
    }
    return HttpResponse(template.render(context, request))

def login_view(request):
    if request.method == 'GET':
        template = loader.get_template("main/login_view.html")
        context = {}
        return HttpResponse(template.render(context, request))
    elif request.method == 'POST':
        submitted_username = request.POST['username']
        submitted_password = request.POST['password']
        user_object = authenticate(
            username=submitted_username,
            password=submitted_password
        )
        if user_object is None:
            messages.add_message(request, messages.INFO, 'Invalid login.')
            return redirect(request.path_info)
        login(request, user_object)
        return redirect('home')


def register_view(request):
    template = loader.get_template("main/register.html")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['confirm_password']

        if password != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    
    context = {

    }

    return HttpResponse(template.render(context, request))

def logout_view(request):
    logout(request)
    return redirect('login')