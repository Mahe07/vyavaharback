# Generated by Django 3.1.3 on 2021-09-02 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20210902_0718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myorder',
            old_name='order_status',
            new_name='status',
        ),
    ]