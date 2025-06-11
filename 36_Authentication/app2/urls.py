from django.contrib import admin
from django.urls import path
from .views import TODO
urlpatterns = [
    path("profile/", TODO,name='profile'),
    
]
