# Generated by Django 3.0.8 on 2020-08-22 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20200819_1326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='order_status',
        ),
    ]