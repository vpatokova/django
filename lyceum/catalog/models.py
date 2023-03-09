import core.models
import django.core.exceptions
import django.core.validators
import django.db
import django.db.models

from tinymce.models import HTMLField

# from django.utils.html import mark_safe

# from sorl.thumbnail import get_thumbnail


def custom_validator(value):
    if "превосходно" not in value and "роскошно" not in value:
        raise django.core.exceptions.ValidationError(
            "В тексте должно быть слово 'превосходно' или 'роскошно'"
        )


class Tag(core.models.AbstractModel, core.models.SlugModel):
    class Meta:
        ordering = ("slug",)
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        default_related_name = "tags"

    def __str__(self):
        return self.name[:15]


class Category(core.models.AbstractModel, core.models.SlugModel):
    weight = django.db.models.PositiveSmallIntegerField(
        default=100,
        verbose_name="вес",
        help_text="значение от 0 до 32767",
    )

    class Meta:
        ordering = ("weight", "id")
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Item(core.models.AbstractModel, core.models.ImageModel):
    is_on_main = django.db.models.BooleanField(default=True)
    text = HTMLField(
        default="Описание товара",
        verbose_name="Описание",
        help_text="Описание должно содержать слова 'превосходно, роскошно'",
        validators=[
            custom_validator,
        ],
    )

    category = django.db.models.ForeignKey(
        Category,
        on_delete=django.db.models.CASCADE,
        default=None,
        null=True,
        blank=True,
        verbose_name="Категория",
    )

    tags = django.db.models.ManyToManyField(
        Tag,
        verbose_name="Тэги",
        default=None,
        blank=True,
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        default_related_name = "items"

    def __str__(self):
        return self.name[:15]


class Image(core.models.ImageModel):
    image = django.db.models.ImageField(
        verbose_name="Изображение",
        help_text="Будет приведено к ширине 1280px",
        default=None,
        null=True,
        blank=True,
        upload_to="catalog",
    )

    item = django.db.models.ForeignKey(
        Item,
        related_name="images",
        on_delete=django.db.models.CASCADE,
        default=None,
        null=True,
        blank=True,
        verbose_name="Товар",
    )

    class Meta:
        ordering = ("id",)
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        default_related_name = "images"
