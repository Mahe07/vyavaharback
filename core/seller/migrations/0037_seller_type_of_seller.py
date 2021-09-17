# Generated by Django 3.1.4 on 2021-03-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0036_remove_seller_type_of_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='type_of_seller',
            field=models.CharField(choices=[('Register', 'Register'), ('Approved', 'Approved'), ('Verified', 'Verified'), ('Draf', 'Draf'), ('Drop', 'Drop')], max_length=100, null=True),
        ),
    ]