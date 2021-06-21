"""
This file was added as part of pages app urls.
"""
# Inbuilt modules
from django.urls import path

# Project modules
from .views import base_listings, individual_listing, search

# 3rd party modules
# N/A

# Global Vars
# N/A

urlpatterns = [path("", base_listings, name = "base_listings"),
        path("<int:listing_id>", individual_listing, name = "ind_listing"),
        path("search", search, name = "listing_search")]
