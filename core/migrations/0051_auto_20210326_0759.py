# Generated by Django 3.1.4 on 2021-03-26 02:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20210325_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 2, 29, 6, 401689, tzinfo=utc)),
        ),
    ]
