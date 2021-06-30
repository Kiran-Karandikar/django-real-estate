from django.contrib import admin

from .models import Contacts


# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    """
    # Docstring
    """
    list_per_page = 25
    list_display = (
    "id", "user_id", "name", "contact_date", "listing", "email", "phone")
    list_display_links = ("id", "name", "user_id")
    search_fields = ("name", "email", "phone")
    list_filter = ("listing",)


admin.site.register(Contacts, ContactsAdmin)
