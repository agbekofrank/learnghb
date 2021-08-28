from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, UserRegisterForm

# Create your views here.

def login_view(req):
    nex = req.GET.get('next')
    # print('1st ', req.user.is_authenticated)
    title = 'login form'
    form = UserLoginForm(req.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(req, user)
        # print('2nd ', req.user.is_authenticated)
        if nex:
            return redirect(nex)
        return redirect('/')
    context = {
        'title': title,
        'form': form
    }
    return render(req, 'auth_form.html', context)

def register_view(req):
    title = 'Register form'
    form = UserRegisterForm(req.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login(req, user)
        return redirect('/')
    context = {
        'title': title,
        'form': form

    }
    return render(req, 'auth_form.html', context)

def logout_view(req):
    logout(req)
    return redirect('/')
