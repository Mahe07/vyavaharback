# Generated by Django 3.1.4 on 2021-06-04 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_cart_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
