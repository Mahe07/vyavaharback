# Generated by Django 3.1.4 on 2021-03-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210325_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_per',
            field=models.IntegerField(null=True),
        ),
    ]
