# Generated by Django 3.1.6 on 2021-02-24 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0012_auto_20210224_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='gstin',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='ref_application_no',
        ),
        migrations.RemoveField(
            model_name='seller_register',
            name='gstin',
        ),
        migrations.RemoveField(
            model_name='seller_register',
            name='ref_application_no',
        ),
    ]
