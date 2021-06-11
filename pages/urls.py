"""
This file was added as part of pages app urls.
"""
# Inbuilt modules
from django.urls import path

# Project modules
from .views import index, about

# 3rd party modules
# N/A

# Global Vars
# N/A
urlpatterns = [
        path("", index, name="home_path"),
        path("index/", index, name="index"),
        path("about/", about, name="about")
]

