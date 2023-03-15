from django.db.models import Prefetch
from django.shortcuts import render
import django.http

from catalog.models import Item, Tag


def home(request):
    template = "homepage/home.html"

    items = (
        Item.objects.filter(is_on_main=True)
        .select_related("category")
        .prefetch_related(
            Prefetch(
                "tags",
                queryset=Tag.objects.filter(is_published=True).only("name"),
            )
        )
        .order_by("name")
        .only("name", "text", "category")
    )
    context = {
        "items": items,
    }

    return render(request, template, context)


def coffee(request):
    return django.http.HttpResponse("<body>I am a teapot</body>")
