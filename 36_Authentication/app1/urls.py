from django.contrib import admin
from django.urls import path
from .views import base,login_view,logout,Register,forget_password,change_pass,todo,delete_view
urlpatterns = [
    path("home/", base,name='home'),
    path("Register/", Register,name='Register'),
    path("login/", login_view,name='login'),
    path("logout/", logout,name='logout'),
    path("change_password/", change_pass,name='change_password'),
    path("forget/",forget_password,name='forget'),

    path('delete/',delete_view,name='delete_account'),
    path("todo/",todo,name='todo'),




]
