# Generated by Django 3.1.6 on 2021-03-05 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210305_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 5, 16, 25, 17, 770965)),
        ),
    ]