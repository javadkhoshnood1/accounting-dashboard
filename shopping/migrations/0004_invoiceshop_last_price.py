# Generated by Django 5.1.2 on 2024-10-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_alter_invoiceshop_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceshop',
            name='last_price',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]
