from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

