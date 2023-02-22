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
    id = django.db.models.PositiveIntegerField(primary_key=True)

    name = django.db.models.CharField(
        default="не указано",
        max_length=150,
        verbose_name="название",
        help_text="max 150 символов",
    )

    is_published = django.db.models.BooleanField(
        default=True,
        verbose_name="опубликовано",
    )

    class Meta:
        abstract = True


class SlugModel(django.db.models.Model):
    slug = django.db.models.SlugField(
        default="",
        validators=[
            django.core.validators.MaxLengthValidator(200),
        ],
        help_text="max 200 символов",
        verbose_name="слаг",
    )

    class Meta:
        abstract = True


class Tag(AbstractModel, SlugModel):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name[:15]


class Category(AbstractModel, SlugModel):
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


class Item(AbstractModel):
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

    tags = django.db.models.ManyToManyField(Tag, verbose_name="Тэги")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name[:15]
