# Generated by Django 3.1.4 on 2021-05-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20210430_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventary',
            name='inventary_status',
        ),
    ]
