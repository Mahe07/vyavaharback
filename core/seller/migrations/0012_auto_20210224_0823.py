# Generated by Django 3.1.6 on 2021-02-24 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0011_seller_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='shop_establishment_certificate',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='seller_register',
            name='shop_establishment_certificate',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.DeleteModel(
            name='Seller_Documents',
        ),
    ]
