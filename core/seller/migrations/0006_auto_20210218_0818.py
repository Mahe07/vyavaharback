# Generated by Django 3.1.6 on 2021-02-18 08:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_auto_20210217_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller_register',
            name='aadhaar_card',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AddField(
            model_name='seller_register',
            name='banking_details',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='seller_register',
            name='org_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='seller_register',
            name='pan_card',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='seller_register',
            name='ref_application_no',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='seller_register',
            name='selling_product',
            field=models.TextField(blank=True),
        ),
    ]
