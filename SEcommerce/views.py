from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        confirm = request.POST['confirm']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        if username is not None and password is not None and firstname is not None and lastname is not None and email is not None and confirm is not None and confirm == password:
            messages.success(request, "Your data has been saved successfully.")
            # return render(request, "SECHTML/signin.html")
        elif username is not None and password is not None and firstname is not None and lastname is not None and email is not None and confirm is not None and confirm != password:
            messages.error(request, "Passwords do not match.")
            return render(request, "SECHTML/signup.html")
        else:
            messages.error(request, "All fields must be filled.")
        return redirect("signup")
    return render(request, "SECHTML/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return render(request, "SECHTML/home.html")
        else:
            messages.error(request, "Incorrect username or password.")
            return render(request, "SECHTML/signin.html")

    return render(request, "SECHTML/signin.html")


def base(request):
    return render(request, "SECHTML/base.html")


def update(request):
    return render(request, "SECHTML/updateprofile.html")


def home(request):
    return render(request, "SECHTML/home.html")


def registration(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        confirm = request.POST['confirm']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        if username is not None and password is not None and firstname is not None and lastname is not None and email is not None and confirm is not None and confirm == password:
            messages.success(request, "Your data has been saved successfully.")
        elif username is not None and password is not None and firstname is not None and lastname is not None and email is not None and confirm is not None and confirm != password:
            messages.error(request, "Passwords do not match.")
            return render(request, "SECHTML/registration.html")
        else:
            messages.error(request, "All fields must be filled.")
        return redirect("registration")
    return render(request, "SECHTML/registration.html")


def switchaccounttype(request):
    return render(request, "SECHTML/switchaccounttype.html")

def sellerreg(request):
    return render(request, "SECHTML/sellerreg.html")