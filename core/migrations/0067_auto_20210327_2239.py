# Generated by Django 3.1.4 on 2021-03-27 17:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20210327_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 17, 9, 10, 5729, tzinfo=utc)),
        ),
    ]