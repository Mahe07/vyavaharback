# Generated by Django 3.1.3 on 2021-09-03 01:15

from django.db import migrations
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20210903_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='weight_scale',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=999999999999, null=True),
        ),
    ]
