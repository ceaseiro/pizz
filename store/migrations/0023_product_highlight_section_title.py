# Generated by Django 4.1.3 on 2023-02-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_product_highlight_include_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='highlight_section_title',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
