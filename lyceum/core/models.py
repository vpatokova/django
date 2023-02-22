import django.db
import django.db.models


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
