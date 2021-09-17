# Generated by Django 3.1.4 on 2021-03-24 12:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0039_auto_20210324_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='aadhaar_card',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='contact_person_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='email_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='gst_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='org_id',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='pan_card',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='seller_status',
            field=models.CharField(choices=[('Register', 'Register'), ('Approved', 'Approved'), ('Verified', 'Verified'), ('Draf', 'Draf'), ('Drop', 'Drop')], default='Register', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='selling_product',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='type_of_seller',
            field=models.CharField(max_length=100, null=True),
        ),
    ]