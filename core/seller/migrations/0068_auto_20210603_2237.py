# Generated by Django 3.1.4 on 2021-06-03 22:37

from django.db import migrations
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0067_auto_20210603_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_logo',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=100, null=True),
        ),
    ]
