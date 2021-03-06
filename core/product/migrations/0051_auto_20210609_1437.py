# Generated by Django 3.1.4 on 2021-06-09 14:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0050_auto_20210609_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku_id',
        ),
        migrations.AddField(
            model_name='pricing',
            name='pricing_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Draft', 'Draft'), ('Declined', 'Declined')], default='Pending', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pricing',
            name='sku_id',
            field=models.TextField(default=uuid.uuid4, null=True),
        ),
    ]
