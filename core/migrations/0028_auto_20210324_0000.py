# Generated by Django 3.1.4 on 2021-03-23 18:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20210324_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 18, 30, 39, 332318, tzinfo=utc)),
        ),
    ]
