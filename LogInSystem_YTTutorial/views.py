from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "LIS/index.html")


def signup(request):
    if request.method == "POST":
        # username = request.POST.get("username")
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

    return render(request, "LIS/signup.html")


def signin(request):
    return render(request, "LIS/signin.html")


def base(request):
    return render(request, "LIS/base.html")


