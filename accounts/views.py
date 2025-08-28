
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm



# Formulário customizado herdando do UserCreationForm
class CustomFormUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


def register_view(request):
    if request.method == 'POST':
        user_form = CustomFormUser(request.POST)
        if user_form.is_valid():
            user_form.save(commit=True)  # garante que o usuário é salvo no banco
            return redirect('login')
    else:
        user_form = CustomFormUser()
    return render(request, 'cadastro.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # redireciona para a própria página
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})



# Create your views here.
