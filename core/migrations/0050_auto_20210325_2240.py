# Generated by Django 3.1.4 on 2021-03-25 17:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_auto_20210325_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 17, 10, 53, 235480, tzinfo=utc)),
        ),
    ]
