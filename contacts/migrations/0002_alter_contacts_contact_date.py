# Generated by Django 3.2.4 on 2021-06-25 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 25, 21, 56, 21, 160156)),
        ),
    ]