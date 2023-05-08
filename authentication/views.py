from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'exp/index.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Paswords do not match.")
            return redirect('signup')
        else:
            if User.objects.filter(username=uname).exists() or User.objects.filter(email=email).exists():
                messages.error(request, "Username or email already exists.")
                return redirect('signup')

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            messages.success(request, "Signup successful. You can now login.")
            return redirect('login')

    return render(request, 'authentication/signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user:
            login(request, user)
            return redirect('index')
        else:
            if not user and username is not None:
                messages.error(request, "Username or password is incorrect.")
                return redirect('login')

    return render(request, 'authentication/login.html')


def LogoutPage(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('login')
