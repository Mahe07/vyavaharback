# Generated by Django 3.1.4 on 2021-04-24 07:49

from django.db import migrations
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0048_remove_seller_banking_passbook_docs'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='banking_passbook_docs',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=999999999999, null=True),
        ),
    ]
