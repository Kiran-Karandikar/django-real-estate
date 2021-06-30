"""
This file was added as part of accounts app urls.
"""
# Inbuilt modules
from django.urls import path

# Project modules
from .views import inquiry

# 3rd party modules
# N/A

# Global Vars
# N/A


urlpatterns = [path("", inquiry, name = "contact_inquiry")]
