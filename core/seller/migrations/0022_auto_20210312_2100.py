# Generated by Django 3.1.6 on 2021-03-12 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0021_auto_20210309_1124'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
