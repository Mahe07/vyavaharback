# Generated by Django 3.1.4 on 2021-04-29 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cart_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
    ]