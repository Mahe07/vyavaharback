# Generated by Django 3.1.4 on 2021-04-29 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0049_seller_banking_passbook_docs'),
        ('product', '0016_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventary_status', models.CharField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Reject', 'Reject')], default='Pending', max_length=100, null=True)),
                ('quantity', models.IntegerField()),
                ('offline_sele_quantity', models.IntegerField()),
                ('online_sele_quantity', models.IntegerField()),
                ('moq_1', models.CharField(max_length=100)),
                ('moq_2', models.CharField(max_length=100)),
                ('moq_3', models.CharField(max_length=100)),
                ('moq_4', models.CharField(max_length=100)),
                ('moq_5', models.CharField(max_length=100)),
                ('moq_price_1', models.IntegerField()),
                ('moq_price_2', models.IntegerField()),
                ('moq_price_3', models.IntegerField()),
                ('moq_price_4', models.IntegerField()),
                ('moq_price_5', models.IntegerField()),
                ('gst', models.IntegerField()),
                ('mrp', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller')),
            ],
            options={
                'verbose_name': 'Inventary',
                'verbose_name_plural': 'Inventarys',
            },
        ),
    ]
