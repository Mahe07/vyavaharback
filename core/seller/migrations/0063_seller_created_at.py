# Generated by Django 3.1.4 on 2021-06-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0062_seller_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
