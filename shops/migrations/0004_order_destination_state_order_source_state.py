# Generated by Django 5.0.3 on 2024-04-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='destination_state',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='source_state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
