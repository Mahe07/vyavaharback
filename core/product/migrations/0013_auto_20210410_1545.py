# Generated by Django 3.1.4 on 2021-04-10 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20210409_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
