# Generated by Django 3.1.4 on 2021-03-26 11:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_auto_20210326_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 11, 8, 54, 96746, tzinfo=utc)),
        ),
    ]
