# Generated by Django 3.1.4 on 2021-06-03 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0064_auto_20210603_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 3, 21, 57, 47, 561186), null=True),
        ),
    ]
