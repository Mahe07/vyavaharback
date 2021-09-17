# Generated by Django 3.1.4 on 2021-03-25 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0042_auto_20210325_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='GST_commission',
            field=models.DecimalField(decimal_places=2, max_digits=999999999, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='gross_commission',
            field=models.DecimalField(decimal_places=2, max_digits=999999999, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='net_commission',
            field=models.DecimalField(decimal_places=2, max_digits=999999999, null=True),
        ),
    ]