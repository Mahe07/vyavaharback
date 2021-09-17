# Generated by Django 3.1.3 on 2021-09-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210830_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='order_status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Pending', 'Pending'), ('Picked', 'Picked'), ('Packed', 'Packed'), ('RTS', 'RTS'), ('In-transit', 'In-transit'), ('Delivered', 'Delivered')], default='Pending', max_length=100, null=True),
        ),
    ]
