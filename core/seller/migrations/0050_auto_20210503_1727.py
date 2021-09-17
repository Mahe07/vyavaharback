# Generated by Django 3.1.4 on 2021-05-03 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0049_seller_banking_passbook_docs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='GST_commission',
            new_name='postpaid_commision',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='gross_commission',
            new_name='prepaid_commision',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='TCS',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='net_commission',
        ),
    ]