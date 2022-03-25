from django.urls import path

from . import views

#app_name = 'crudapi'

urlpatterns = [
    
    path("Register", views.register, name="register"),
    path("Home", views.index, name="index"),
     path("", views.loginview, name="login"),
    path("Logout", views.logoutview, name="logout"),
]