# Generated by Django 3.1.4 on 2021-03-24 13:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20210324_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 24, 13, 0, 54, 509491, tzinfo=utc)),
        ),
    ]
