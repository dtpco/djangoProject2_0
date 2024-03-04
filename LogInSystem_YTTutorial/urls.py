from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup')
]
