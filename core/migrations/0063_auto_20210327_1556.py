# Generated by Django 3.1.4 on 2021-03-27 10:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_auto_20210327_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 10, 26, 41, 388802, tzinfo=utc)),
        ),
    ]