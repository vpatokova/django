import django.db.models


class Feedback(django.db.models.Model):
    text = django.db.models.CharField(
        max_length=1500,
        verbose_name="Текст обратной связи",
    )
    created_on = django.db.models.DateTimeField(
        auto_now_add=True,
    )
    mail = django.db.models.EmailField()
