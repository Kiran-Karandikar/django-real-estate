"""
# Model file for Realtors app
"""
from datetime import datetime
from django.db import models


class Realtor(models.Model):
    """
    # docstring
    """
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 100, blank = True)
    photo = models.ImageField(upload_to = "photos/realtor/%Y-%m-%d")
    is_mvp = models.BooleanField(default = False)
    hire_date = models.DateField(default = datetime.now(), blank = True)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
