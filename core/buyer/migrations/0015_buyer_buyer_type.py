# Generated by Django 3.1.4 on 2021-06-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0014_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='buyer_type',
            field=models.CharField(blank=True, choices=[('Retailer', 'Retailer'), ('Commision_Agent', 'Commision_Agent')], max_length=100, null=True),
        ),
    ]