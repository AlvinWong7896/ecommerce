# Generated by Django 4.2.5 on 2023-12-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(default='na', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(default='na', max_length=200, null=True),
        ),
    ]
