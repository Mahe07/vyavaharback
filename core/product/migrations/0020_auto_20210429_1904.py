# Generated by Django 3.1.4 on 2021-04-29 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_auto_20210429_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventary',
            old_name='seller_id',
            new_name='seller',
        ),
    ]
