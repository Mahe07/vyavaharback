# Generated by Django 3.1.4 on 2021-04-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_auto_20210429_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='return_day',
        ),
        migrations.AddField(
            model_name='inventary',
            name='return_day',
            field=models.IntegerField(null=True),
        ),
    ]
