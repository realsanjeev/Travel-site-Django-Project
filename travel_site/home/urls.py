from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('places', views.places, name="places"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('signup', views.register_user, name="register_user")
]