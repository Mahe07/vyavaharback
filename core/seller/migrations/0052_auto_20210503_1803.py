# Generated by Django 3.1.4 on 2021-05-03 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0051_auto_20210503_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='postpaid_commision',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='prepaid_commision',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]