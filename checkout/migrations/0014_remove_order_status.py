# Generated by Django 3.0.8 on 2020-08-23 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]