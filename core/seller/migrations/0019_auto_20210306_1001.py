# Generated by Django 3.1.6 on 2021-03-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0018_delete_loginotp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_status',
            field=models.CharField(choices=[('Register', 'Register'), ('Approved', 'Approved'), ('Decline', 'Decline'), ('Draf', 'Draf'), ('Drop', 'Drop')], default='Register', max_length=100),
        ),
    ]