# Generated by Django 3.1.3 on 2021-08-24 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buyer', '0017_auto_20210605_1309'),
        ('seller', '0069_auto_20210603_2237'),
        ('product', '0056_inventory_out_of_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='myorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='buyer.buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='seller.seller')),
            ],
        ),
    ]