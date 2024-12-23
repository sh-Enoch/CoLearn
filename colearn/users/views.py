from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import CustomUser as User
from .forms import UserRegistrationForm
from django.urls import reverse

# Create your views here.

"""Create a user registration view"""
class SignUpView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = UserRegistrationForm
   
    def get_success_url(self):
       return reverse('login')
    




