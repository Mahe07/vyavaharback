# Generated by Django 3.1.6 on 2021-03-06 04:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210306_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 4, 39, 26, 951798, tzinfo=utc)),
        ),
    ]
