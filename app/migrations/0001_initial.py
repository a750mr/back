# Generated by Django 4.1.2 on 2022-11-05 23:23

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=40, validators=[app.models.MyValidation.check_name_and_city])),
                ('country', models.CharField(choices=[('USA', 'USA'), ('Canada', 'Canada'), ('Belarus', 'Belarus'), ('Ukraine', 'Ukraine'), ('Germany', 'Germany'), ('France', 'France'), ('Great Britain', 'Great Britain'), ('Russia', 'Russia')], max_length=30)),
                ('city', models.CharField(max_length=20, validators=[app.models.MyValidation.check_name_and_city])),
                ('address', models.CharField(max_length=40, validators=[app.models.MyValidation.check_address])),
                ('phone', models.CharField(max_length=20, validators=[app.models.MyValidation.check_number, django.core.validators.MinLengthValidator(10)])),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('note', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, validators=[app.models.MyValidation.check_address, django.core.validators.MinLengthValidator(3)])),
                ('amount', models.CharField(max_length=3, validators=[app.models.MyValidation.only_int])),
                ('price', models.CharField(max_length=5, validators=[app.models.MyValidation.only_int_and_great_null])),
                ('manufacturer', models.CharField(max_length=100, validators=[app.models.MyValidation.check_name_and_city, django.core.validators.MinLengthValidator(3)])),
                ('notes', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('delivery', models.CharField(choices=[('Pickup', 'Pickup'), ('Delivery', 'Delivery')], max_length=40)),
                ('delivery_date', models.DateField()),
                ('order_status', models.CharField(choices=[('Draft', 'Draft'), ('Open', 'Open'), ('Partially Received', 'Partially Received'), ('Received', 'Received'), ('Cancelled', 'Cancelled')], max_length=40)),
                ('total_price', models.CharField(max_length=10)),
                ('costumer', models.ManyToManyField(to='app.costumers')),
                ('products', models.ManyToManyField(to='app.products')),
            ],
        ),
    ]
