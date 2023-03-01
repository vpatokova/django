import django.db
import django.db.models
from django.utils.html import mark_safe

from sorl.thumbnail import get_thumbnail


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


class ImageModel(django.db.models.Model):
    image = django.db.models.ImageField(
        "Будет приведено к ширине 1280px",
        default=None,
        upload_to="uploads/% Y/% m/% d/",
    )

    def get_image_x1280(self):
        return get_thumbnail(self.image, "1280", quality=51)

    def get_image_400x300(self):
        return get_thumbnail(self.image, "400x300", crop="center", quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f"<img src='{self.image.url}' width='50'>"
            )
        return "Нет изображения"

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    list_display = (
        "image_tmb"
    )

    class Meta:
        abstract = True
