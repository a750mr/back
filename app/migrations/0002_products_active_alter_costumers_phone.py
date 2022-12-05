# Generated by Django 4.1.2 on 2022-11-28 20:07

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='costumers',
            name='phone',
            field=models.CharField(max_length=21, validators=[app.models.MyValidation.check_number, django.core.validators.MinLengthValidator(11)]),
        ),
    ]