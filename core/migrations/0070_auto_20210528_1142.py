# Generated by Django 3.1.4 on 2021-05-28 06:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_email_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_otp',
            name='valid_till',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 11, 57, 4, 496995)),
        ),
        migrations.AlterField(
            model_name='loginotp',
            name='valid_till',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 11, 57, 4, 496995)),
        ),
    ]
