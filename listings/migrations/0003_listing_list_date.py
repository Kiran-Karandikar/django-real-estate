# Generated by Django 3.2.4 on 2021-06-17 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_remove_listing_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='list_date',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 17, 54, 39, 149874)),
        ),
    ]
