import django.db


class Item(django.db.models.Model):
    name = django.db.models.TextField()
