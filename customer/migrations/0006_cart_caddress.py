# Generated by Django 5.0.6 on 2024-07-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_remove_order_cdish_order_customer_order_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='caddress',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
