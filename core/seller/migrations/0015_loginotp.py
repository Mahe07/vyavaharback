# Generated by Django 3.1.6 on 2021-02-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0014_auto_20210224_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginOtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=10)),
                ('otp', models.CharField(max_length=6)),
                ('valid_till', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'LoginOtp',
                'verbose_name_plural': 'LoginOtps',
            },
        ),
    ]
