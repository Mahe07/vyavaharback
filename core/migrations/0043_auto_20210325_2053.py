# Generated by Django 3.1.4 on 2021-03-25 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20210325_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 15, 23, 51, 508009, tzinfo=utc)),
        ),
    ]
