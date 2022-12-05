import re

from django.core.validators import MinLengthValidator
from django.db import models
from rest_framework.exceptions import ValidationError


class MyValidation:
    @staticmethod
    def check_name_and_city(name):
        if re.match(r'^[a-zA-Z ]+$', name):
            return name
        else:
            raise ValidationError("EBLAN, VVEDI NORMANLNOE NAME")

    @staticmethod
    def check_address(address):
        if re.match(r'^[A-Za-z0-9 ]*[A-Za-z0-9][A-Za-z0-9 ]*$', address):
            return address
        else:
            raise ValidationError("EBLAN, VVEDI NORMANLNIU ADDRESS")

    @staticmethod
    def check_number(number):
        if re.match(r'^\+?[1-9][0-9]+$', number):
            return number
        else:
            raise ValidationError('nomer vvedi normalniu')

    @staticmethod
    def only_int(value):
        if not value.isdigit():
            raise ValidationError('ID contains have characters')

    @staticmethod
    def only_int_and_great_null(value):
        if not value.isdigit() or int(value) < 1:
            raise ValidationError('ID contains have characters')


class Costumers(models.Model):
    coutry_choises = (("USA", "USA"),
                      ("Canada", "Canada"),
                      ("Belarus", "Belarus"),
                      ("Ukraine", "Ukraine"),
                      ("Germany", "Germany"),
                      ("France", "France"),
                      ("Great Britain", "Great Britain"),
                      ("Russia", "Russia"))

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=40, validators=[MyValidation.check_name_and_city])
    country = models.CharField(max_length=30, choices=coutry_choises)
    city = models.CharField(max_length=20, validators=[MyValidation.check_name_and_city])
    address = models.CharField(max_length=40, validators=[MyValidation.check_address])
    phone = models.CharField(max_length=21, validators=[MyValidation.check_number, MinLengthValidator(11)])
    date_create = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.name}"


class Products(models.Model):
    name = models.CharField(unique=True, max_length=40, validators=[MyValidation.check_address, MinLengthValidator(3)])
    amount = models.CharField(max_length=3, validators=[MyValidation.only_int])
    price = models.CharField(max_length=5, validators=[MyValidation.only_int_and_great_null])
    manufacturer = models.CharField(max_length=100,
                                    validators=[MyValidation.check_name_and_city, MinLengthValidator(3)])
    notes = models.CharField(max_length=250, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Orders(models.Model):
    delivery_model_choices = (("Pickup", "Pickup"),
                              ("Delivery", "Delivery"))
    order_status_choices = (("Draft", "Draft"),
                            ("Open", "Open"),
                            ("Partially Received", "Partially Received"),
                            ("Received", "Received"),
                            ("Cancelled", "Cancelled"))
    costumer = models.ManyToManyField(Costumers)
    products = models.ManyToManyField(Products)
    date_create = models.DateTimeField(auto_now_add=True)
    delivery = models.CharField(max_length=40, choices=delivery_model_choices)
    delivery_date = models.DateField()
    order_status = models.CharField(max_length=40, choices=order_status_choices)
    total_price = models.CharField(max_length=10)
