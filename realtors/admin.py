from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    """
    Docstring.
    """
    list_display = ("id", "name", "is_mvp", "phone", "email")
    list_display_links = ("id", "name")
    list_editable = ("is_mvp",)
    list_filter = ("is_mvp", )
    list_per_page = 10
    # todo
    # this shows the fields to search for just one field not for more than field
    search_fields = ("name",)


# Register your models here.
admin.site.register(Realtor, RealtorAdmin)

