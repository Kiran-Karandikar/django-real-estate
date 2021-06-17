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
# todo
# Defect
# if you go to about page and then click on breadcru index, this doesn't work ,
# has to do with some url followings
urlpatterns = [
        path("", index, name="home_path"),
        path("index/", index, name="index"),
        path("about/", about, name="about")
]
