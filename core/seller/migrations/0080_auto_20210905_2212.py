# Generated by Django 3.1.3 on 2021-09-05 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0079_auto_20210905_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='postpaid_commision',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='prepaid_commision',
        ),
        migrations.AddField(
            model_name='transaction_details',
            name='postpaid_commision',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction_details',
            name='prepaid_commision',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
