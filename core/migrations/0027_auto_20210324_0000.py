# Generated by Django 3.1.4 on 2021-03-23 18:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20210323_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 18, 30, 5, 583592, tzinfo=utc)),
        ),
    ]