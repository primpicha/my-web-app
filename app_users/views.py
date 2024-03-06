from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login

from app_users.forms import RegisterForm
# Create your views here.

def register(request: HttpRequest):
    # Default
    form = RegisterForm()

    # POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Register and wait for activation
           # user: CustomUser = form.save(commit=False)
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse("home"))
        else:
            pass # assign in default
            # form = RegisterForm()
      

    # GET
    context = {"form": form}
    return render(request, "app_users/register.html", context)

def register_thankyou(request):
    return render(request, "app_users/register_thankyou.html")

def dashboard(request):
    return render(request, "app_users/dashboard.html")

def profile(request):
    return render(request, "app_users/profile.html")