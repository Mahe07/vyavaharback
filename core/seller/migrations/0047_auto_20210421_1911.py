# Generated by Django 3.1.4 on 2021-04-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0046_auto_20210421_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='aadhaar_card',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='gst_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='pan_card',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='type_of_seller',
            field=models.CharField(max_length=100, null=True),
        ),
    ]