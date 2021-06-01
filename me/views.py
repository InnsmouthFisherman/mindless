from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, \
                                      DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, \
                                       PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.forms.models import modelform_factory
from django.apps import apps
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from .models import Teacher
from .forms import UserRegistrationForm, UserLoginForm
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'teachers/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'teachers/registration.html', {'user_form': user_form})

def profile_view(request):
    pass

def authentication(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            try:
                user = Teacher.objects.get(password=user_form['password'])
                user.authenticate()
            except ObjectDoesNotExist:
                nothing = None
                return render(request, 'teachers/login_error.html', {'nothing': nothing})
    else:
        user_form = UserLoginForm()
        return render(request, 'teachers/login.html', {'user_form': user_form})
