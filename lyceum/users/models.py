from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    birthday = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name="Аватарка",
        blank=True,
        null=True,
    )
    coffee_count = models.PositiveIntegerField(
        verbose_name="Чашки кофе",
    )

    class Meta:
        verbose_name = "Дополнительное поле"
        verbose_name_plural = "Дополнительные поля"
