import django.http
import django.shortcuts

import catalog.models


def home(request):
    template = "homepage/home.html"
    """
    my_ids = (
        catalog.models.Item.objects.filter(is_on_main=True).
        values_list("id", flat=True)
    )
    if my_ids:
        items = catalog.models.Item.objects.filter(
            id__in=[random.choice(my_ids), random.choice(my_ids)],
        )
    else:
        items = None
    """
    items = (
        catalog.models.Item.objects.filter(is_on_main=True)
        .select_related("category")
        .prefetch_related(
            django.db.models.Prefetch(
                "tags",
                queryset=catalog.models.Tag.objects.filter(
                    is_published=True
                ).only("name"),
            )
        )
        .order_by("name")
        .only("name", "text", "category")
    )
    context = {
        "items": items,
    }

    context = {
        "items": items,
    }
    return django.shortcuts.render(request, template, context)


def coffee(request):
    return django.http.HttpResponse("<body>I am a teapot</body>", status=418)
