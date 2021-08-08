from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from . forms import SignUpForm


# Create your views here.
def signup(response):
    if response.method == "POST":
        reg_form = SignUpForm(response.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect("/")
    else:
        reg_form= SignUpForm()
    return render(response,"signup/sign-up.html",{"reg_form": reg_form})