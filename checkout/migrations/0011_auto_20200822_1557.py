# Generated by Django 3.0.8 on 2020-08-22 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_auto_20200822_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_status',
            new_name='status',
        ),
    ]