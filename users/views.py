from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm


# Create your views here.

def signup_user(request):
    form = SignUpForm()
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    return render(request, 'login.html')

def login_submit(request):
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e/ou senha inválidos')
    else:
        messages.error(request, 'Usuário e/ou senha inválidos')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
