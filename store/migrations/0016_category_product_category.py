# Generated by Django 4.1.3 on 2023-02-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_delete_combo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Categories')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='combos', to='store.category'),
        ),
    ]