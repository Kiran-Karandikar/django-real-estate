"""
# Docstring
"""
from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    """
    # Docstring
    """
    list_display = ("id", "title", "is_published", "city", "state", "zipcode")
    list_display_links = ("id", "title")
    list_editable = ("is_published",)
    list_filter = ("city", "state", "zipcode", "realtor")
    list_per_page = 10
    # todo
    # this shows the fields to search for just one field not for more than field
    search_fields = ("title",)


# Register your models here.
admin.site.register(Listing, ListingAdmin)
