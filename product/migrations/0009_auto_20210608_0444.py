# Generated by Django 2.2.24 on 2021-06-08 01:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0008_auto_20210608_0415'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentForProduct',
            new_name='Review',
        ),
        migrations.AlterModelTable(
            name='review',
            table='Reviews',
        ),
    ]