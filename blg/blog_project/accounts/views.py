from django.shortcuts import render

# Create your views here.
from django.db import models
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url =reverse_lazy('login')
    template_name = 'signup.html'
    
