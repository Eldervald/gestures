from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from login.forms import *
from login.backend import *


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class LoginUserWithVideo(LoginView):
    form_class = LoginUserWithVideoForm
    template_name = 'users/loginWithVideo.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
