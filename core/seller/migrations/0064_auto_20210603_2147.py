# Generated by Django 3.1.4 on 2021-06-03 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0063_seller_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='adhaar_card',
            new_name='aadhaar_card',
        ),
    ]
