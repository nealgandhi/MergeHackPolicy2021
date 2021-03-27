from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404


def index(request):
    if request.user.is_authenticated:
        auth = {"auth_url": "accounts/logout", "auth_text": "Logout"}
    else:
        auth = {"auth_url": "accounts/login", "auth_text": "Login"}
    return render(request, 'index.html', auth)


def auction(request):
    if request.user.is_authenticated:
        auth = {"auth_url": "accounts/logout", "auth_text": "Logout"}
    else:
        auth = {"auth_url": "accounts/login", "auth_text": "Login"}
    return render(request, 'auction.html', auth)


def sign_up(request):
    if request.user.is_authenticated:
        raise Http404("Can't sign up if you're logged in already")
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'index.html')
    context['form'] = form
    return render(request, 'registration/sign_up.html', context)
