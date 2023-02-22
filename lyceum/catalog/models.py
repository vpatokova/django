import django.core.exceptions
import django.core.validators
import django.db
import django.db.models


def custom_validator(value):
    if "превосходно" not in value and "роскошно" not in value:
        raise django.core.exceptions.ValidationError(
            "В тексте должно быть слово 'превосходно' или 'роскошно'"
        )


class AbstractModel(django.db.models.Model):
    name = django.db.models.TextField()

    class Meta:
        abstract = True


class Tag(django.db.models.Model):
    id = django.db.models.PositiveIntegerField(primary_key=True)

    name = django.db.models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="max 150 символов",
    )

    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name="опубликовано",
    )

    slug = django.db.models.SlugField(
        default="",
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        help_text="max 200 символов",
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name[:15]


class Category(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name="опубликовано",
    )

    id = django.db.models.PositiveIntegerField(
        primary_key=True,
    )

    name = django.db.models.CharField(
        default="не указано",
        max_length=150,
        verbose_name="название",
        help_text="max 150 символов",
    )

    slug = django.db.models.SlugField(
        default="",
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        help_text="max 200 символов",
    )

    weight = django.db.models.PositiveSmallIntegerField(
        default=100,
        verbose_name="вес",
        help_text="значение от 0 до 32767",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Item(django.db.models.Model):
    id = django.db.models.PositiveIntegerField(primary_key=True)

    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name="опубликовано",
    )

    name = django.db.models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="max 150 символов",
    )

    text = django.db.models.TextField(
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

    tags = django.db.models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:15]
