"""
This file was added as part of accounts app urls.
"""
# Inbuilt modules
from django.urls import path

# Project modules
from .views import dashboard, login, logout, register

# 3rd party modules
# N/A

# Global Vars
# N/A


urlpatterns = [path("register", register, name = "register"),
        path("login", login, name = "login"),
        path("logout", logout, name = "logout"),
        path("dashboard", dashboard, name = "dashboard"), ]
