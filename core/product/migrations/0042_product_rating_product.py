# Generated by Django 3.1.4 on 2021-05-14 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0041_auto_20210514_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_rating',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]