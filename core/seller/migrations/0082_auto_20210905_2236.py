# Generated by Django 3.1.3 on 2021-09-05 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0081_auto_20210905_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='order_type',
        ),
        migrations.DeleteModel(
            name='transaction_details',
        ),
    ]
