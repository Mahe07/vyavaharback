# Generated by Django 3.1.4 on 2021-05-29 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_auto_20210529_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_otp',
            name='valid_till',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='loginotp',
            name='valid_till',
            field=models.DateTimeField(null=True),
        ),
    ]
