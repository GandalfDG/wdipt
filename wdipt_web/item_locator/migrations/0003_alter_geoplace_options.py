# Generated by Django 5.1.6 on 2025-02-27 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("item_locator", "0002_storageplace_item"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="geoplace",
            options={"verbose_name": "geographic location"},
        ),
    ]
