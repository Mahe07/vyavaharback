# Generated by Django 3.1.4 on 2021-06-09 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0053_auto_20210609_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricing',
            name='product',
        ),
        migrations.RemoveField(
            model_name='pricing',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
        migrations.DeleteModel(
            name='Pricing',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
