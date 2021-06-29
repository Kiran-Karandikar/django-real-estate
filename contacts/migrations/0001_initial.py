# Generated by Django 3.2.4 on 2021-06-25 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.IntegerField()),
                ('listing', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, max_length=300)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 25, 21, 55, 48, 660375))),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]