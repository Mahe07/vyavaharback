# Generated by Django 3.1.4 on 2021-03-25 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='added_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
    ]
