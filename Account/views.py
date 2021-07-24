from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import AccountAuthenticationForm, RegistrationForm, ProfileForm
from .models import Account, Profile
from django.contrib.auth import get_user_model
from django_email_verification import send_email
from django.http import JsonResponse
from django.core import serializers

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()
        context['login_form'] = form

    return render(request, "login.html", context)


def registration_view(request):
    context = {}
    if request.POST and request.is_ajax:
        form = RegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid():
            print("success")
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            send_email(user)
            # send to client side.
            return JsonResponse({"instance": 
                                "An email has been sent to your registered email id please verify to activate your account"}, 
                                status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def dashboard(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return render(request, "dashboard.html", context)
