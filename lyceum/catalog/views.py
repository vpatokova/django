from django.http import HttpResponse
import django.db.models
import django.shortcuts

import catalog.models


def item_list(request):
    template = "catalog/list.html"
    items = (
        catalog.models.Item.objects.filter(is_published=True)
        .select_related("category")
        .prefetch_related(
            django.db.models.Prefetch(
                "tags",
                queryset=catalog.models.Tag.objects.filter(
                    is_published=True
                ).only("name"),
            )
        )
        .order_by("category")
        .only("name", "text", "category")
    )
    context = {
        "items": items,
    }
    return django.shortcuts.render(request, template, context)


def item_detail(request, pk):
    template = "catalog/detail.html"
    item = django.shortcuts.get_object_or_404(
        catalog.models.Item.objects.filter(is_published=True)
        .select_related("category")
        .prefetch_related(
            django.db.models.Prefetch(
                "tags",
                queryset=catalog.models.Tag.objects.filter(
                    is_published=True
                ).only("name"),
            )
        ),
        pk=pk,
    )
    images = (
        catalog.models.Image.objects.filter(item_id=pk)
        .order_by("id")
        .only("image")
    )
    context = {
        "item": item,
        "images": images,
    }
    return django.shortcuts.render(request, template, context)


def new_page(request):
    return HttpResponse("<body>Я родился!</body>")


def converter(request, text, number):
    return HttpResponse(
        f"<body>I'm a converter!. Text is {text}, number is {number}</body>"
    )
