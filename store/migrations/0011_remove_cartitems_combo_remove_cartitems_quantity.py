# Generated by Django 4.1.3 on 2023-02-03 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_cartitems_combo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='combo',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='quantity',
        ),
    ]
