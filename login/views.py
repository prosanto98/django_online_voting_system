from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignUpForm
from .models import voter
import hashlib


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("signup_success")
    template_name = "signup.html"


def signup_success(request):
    return render(request, "signup_success.html")


# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = voter.objects.get(email=email)
            hashed_input_password = hash_password(password)
            if user.password == hashed_input_password:
                request.session["user_id"] = user.id
                return redirect("login_ok")
            else:
                error_message = "Invalid password"
        except voter.DoesNotExist:
            error_message = "Invalid email"
        return render(request, "login.html", {"error_message": error_message})
    else:
        return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            hashed_password = hash_password(password)
            user.password = hashed_password
            user.save()
            return redirect("signup_success")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def forgot_password(request):
    return render(request, "forgot_password.html")


# ✅ Main login_ok that sends user_email for gravatar
def login_ok(request):
    user_email = None
    user_id = request.session.get("user_id")
    if user_id:
        try:
            user = voter.objects.get(id=user_id)
            user_email = user.email
        except voter.DoesNotExist:
            pass
    return render(request, "login_ok.html", {"user_email": user_email})


# ✅ Logout view
def logout_view(request):
    try:
        del request.session["user_id"]
    except KeyError:
        pass
    return redirect("login")