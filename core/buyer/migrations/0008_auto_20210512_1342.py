# Generated by Django 3.1.4 on 2021-05-12 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0007_auto_20210511_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='first_name',
            new_name='owner_name',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='last_name',
        ),
    ]
