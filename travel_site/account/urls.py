from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('profile/<str:username>/', views.account_view, name="profile"),
    path('logout', views.logout_user, name="logout"),
    path('signup', views.register_user, name="register-user"),
]