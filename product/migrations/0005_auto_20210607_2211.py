# Generated by Django 2.2.24 on 2021-06-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210607_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='', verbose_name='Изображение товара'),
        ),
    ]
