# Generated by Django 3.1.3 on 2021-08-25 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorder',
            name='seller',
        ),
    ]
