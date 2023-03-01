# Generated by Django 3.2.15 on 2023-03-01 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0005_auto_20230301_1754"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="catalog/",
                        verbose_name="Будет приведено к ширине 1280px",
                    ),
                ),
            ],
            options={
                "verbose_name": "Изображение",
                "verbose_name_plural": "Изображения",
            },
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Item",
                to="catalog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="main_image",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to="uploads",
                verbose_name="Главное изображение",
            ),
        ),
    ]
