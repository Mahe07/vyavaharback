# Generated by Django 3.1.6 on 2021-02-24 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0013_auto_20210224_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='seller_register',
            name='profile_image',
        ),
    ]