from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"LogInSystem_YTTutorial/home.html")
def signup(request):
    return render(request,"LogInSystem_YTTutorial/signup.html")

def signin(request):
    return render(request,"LogInSystem_YTTutorial/signin.html")

def signout(request):
    pass