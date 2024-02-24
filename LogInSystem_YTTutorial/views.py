from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "LIS/../templates/index.html")


def signup(request):
    if request.method == "POST":
        # username = request.POST.get("username")
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()

        messages.success(request, "Your account has been successfully created.")
        return redirect("signin")
    return render(request, "LIS/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "LIS/home.html")
        else:
            messages.error(request, "Invalid")
            return redirect("index")

    return render(request, "LIS/signin.html")


def base(request):
    return render(request, "LIS/base.html")


def home(request):
    return render(request, "LIS/home.html")
