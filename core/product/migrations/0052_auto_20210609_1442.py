# Generated by Django 3.1.4 on 2021-06-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0051_auto_20210609_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tittle',
            field=models.TextField(null=True),
        ),
    ]
