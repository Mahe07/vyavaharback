# Generated by Django 3.1.4 on 2021-06-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0052_auto_20210609_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='offer_details',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='offer_end_date',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='offer_start_date',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='offer_stock',
        ),
        migrations.AddField(
            model_name='pricing',
            name='offer_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='offer_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='offer_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='offer_stock',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
