# Generated by Django 4.1.3 on 2022-12-07 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
