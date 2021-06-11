"""
This file was added as part of pages app urls.
"""
# Inbuilt modules
from django.urls import path

# Project modules
from .views import listing_home

# 3rd party modules
# N/A

# Global Vars
# N/A
urlpatterns = [
        path("", listing_home, name="listings_home"),
]

