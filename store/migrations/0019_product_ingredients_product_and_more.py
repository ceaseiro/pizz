# Generated by Django 4.1.3 on 2023-02-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_product_combo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ingredients_product',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description_product',
            field=models.TextField(max_length=1000),
        ),
    ]