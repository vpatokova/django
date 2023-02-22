# Generated by Django 3.2.15 on 2023-02-22 15:50

import catalog.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "is_published",
                    models.BooleanField(default=True, verbose_name="опубликовано"),
                ),
                (
                    "name",
                    models.CharField(
                        default="not specified",
                        help_text="max 150 символов",
                        max_length=150,
                        verbose_name="название",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        default="",
                        help_text="max 200 символов",
                        validators=[django.core.validators.MaxLengthValidator(200)],
                    ),
                ),
                (
                    "weight",
                    models.PositiveSmallIntegerField(
                        default=100,
                        help_text="значение от 0 до 32767",
                        verbose_name="вес",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.PositiveIntegerField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        help_text="max 150 символов",
                        max_length=150,
                        verbose_name="название",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(default=True, verbose_name="опубликовано"),
                ),
                (
                    "slug",
                    models.SlugField(
                        default="",
                        help_text="max 200 символов",
                        validators=[django.core.validators.MaxLengthValidator(200)],
                    ),
                ),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
            },
        ),
        migrations.AlterModelOptions(
            name="item",
            options={"verbose_name": "Товар", "verbose_name_plural": "Товары"},
        ),
        migrations.AddField(
            model_name="item",
            name="is_published",
            field=models.BooleanField(default=True, verbose_name="опубликовано"),
        ),
        migrations.AddField(
            model_name="item",
            name="text",
            field=models.TextField(
                default="роскошное пустое описание",
                help_text="Описание должно содержать слова 'превосходно, роскошно'",
                validators=[catalog.models.custom_validator],
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="name",
            field=models.CharField(
                help_text="max 150 символов", max_length=150, verbose_name="название"
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="tags",
            field=models.ManyToManyField(to="catalog.Tag"),
        ),
    ]