import datetime

import django.db.models


class Feedback(django.db.models.Model):
    text = django.db.models.CharField(
        default="не указано",
        max_length=1500,
        verbose_name="Текст обратной связи",
    )
    created_on = django.db.models.DateTimeField(
        default=datetime.datetime.now(),
    )
    mail = django.db.models.EmailField()
