# Generated by Django 3.1.3 on 2021-09-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0078_auto_20210905_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ldc_details',
            name='certificate_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaction_details',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]