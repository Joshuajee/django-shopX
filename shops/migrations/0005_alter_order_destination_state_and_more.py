# Generated by Django 5.0.3 on 2024-04-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_order_destination_state_order_source_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination_state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='source_state',
            field=models.CharField(max_length=50),
        ),
    ]
