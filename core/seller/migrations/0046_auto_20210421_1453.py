# Generated by Django 3.1.4 on 2021-04-21 09:23

from django.db import migrations
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0045_auto_20210421_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='banking_passbook',
            new_name='aadhaar_docs',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='cancelled_ca_cheque',
            new_name='banking_passbook_docs',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='drug_licence',
            new_name='cancelled_cheque_docs',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='scale_licence',
            new_name='drug_docs',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='trade_licence',
            new_name='pan_docs',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='udhyaam',
            new_name='scale_docs',
        ),
        migrations.AddField(
            model_name='seller',
            name='trade_docs',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=999999999999, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='udhyaam_docs',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=999999999999, null=True),
        ),
    ]
