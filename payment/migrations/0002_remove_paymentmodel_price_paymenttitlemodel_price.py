# Generated by Django 5.1 on 2024-08-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmodel',
            name='price',
        ),
        migrations.AddField(
            model_name='paymenttitlemodel',
            name='price',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]
