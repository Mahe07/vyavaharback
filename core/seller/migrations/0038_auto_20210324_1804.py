# Generated by Django 3.1.4 on 2021-03-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0037_seller_type_of_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='type_of_seller',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
