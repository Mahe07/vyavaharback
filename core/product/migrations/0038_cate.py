# Generated by Django 3.1.4 on 2021-05-14 10:02

from django.db import migrations, models
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_auto_20210514_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(default=0)),
                ('category_name', models.CharField(max_length=200, null=True)),
                ('category_image', django_base64field.fields.Base64Field(blank=True, default='', max_length=999999999, null=True)),
            ],
        ),
    ]
