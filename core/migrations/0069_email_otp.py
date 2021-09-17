# Generated by Django 3.1.4 on 2021-04-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_delete_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_Otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=10)),
                ('otp', models.CharField(max_length=6)),
                ('valid_till', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Email_Otp',
                'verbose_name_plural': 'Email_Otps',
            },
        ),
    ]
