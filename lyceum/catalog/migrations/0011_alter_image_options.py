# Generated by Django 3.2.15 on 2023-03-22 11:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0010_auto_20230308_1212"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={
                "default_related_name": "images",
                "ordering": ("id",),
                "verbose_name": "Изображение",
                "verbose_name_plural": "Изображения",
            },
        ),
    ]