# Generated by Django 3.1.6 on 2021-03-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='logout_time',
            field=models.DateTimeField(null=True),
        ),
    ]