# Generated by Django 3.1.6 on 2021-02-17 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categorys'},
        ),
    ]
