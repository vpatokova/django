from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag, Image


def item_list(request):
    template = "catalog/list.html"
    items = (
        Item.objects.filter(is_published=True)
        .select_related("category")
        .prefetch_related(
            Prefetch(
                "tags",
                queryset=Tag.objects.filter(is_published=True).only("name"),
            )
        )
        .order_by("category")
        .only("name", "text", "category")
    )
    context = {
        "items": items,
    }
    return render(request, template, context)


def item_detail(request, pk):
    template = "catalog/detail.html"
    item = get_object_or_404(
        Item.objects.filter(is_published=True)
        .select_related("category")
        .prefetch_related(
            Prefetch(
                "tags",
                queryset=Tag.objects.filter(is_published=True).only("name"),
            ),
            Prefetch(
                "images",
                queryset=Image.objects.only("image"),
            ),
        ),
        pk=pk,
    )

    context = {
        "item": item,
    }
    return render(request, template, context)


'''
def item_create(request):
    template = "create.html"
    form = ItemForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data["name"]
        Item.objects.create(name=name)
    context = {
        "form": form,
    }
    return render(request, template, context)


def item_delete(request, pk):
    template = "delete.html"
    item = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        item.delete()
    context = {
        "item": item,
    }
    return render(request, template, context)


def item_update(request, pk):
    template = "update.html"
    item = get_object_or_404(Tag, pk=pk)
    form = ItemForm(request.POST or None)

    if form.is_valid():
        item.name = form.cleaned_data["name"]
        item.save(update_fields=["name"])
    context = {
        "form": form,
    }
    return render(request, template, context)


def tag_create(request):
    template = "catalog/tag_create.html"
    form = TagCreateForm(request.POST or None)
    if form.is_valid():
        is_published = form.cleaned_data["is_published"]
        name = form.cleaned_data["name"]
        slug = form.cleaned_data["slug"]
        Tag.objects.create(
            is_published=is_published,
            name=name,
            slug=slug,
        )
        return redirect("catalog:tag_create")
    context = {
        "form": form,
    }
    return render(request, template, context)


def tag_delete(request, pk):
    template = "catalog/tag_delete.html"
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
    context = {
        "tag": tag,
    }
    return render(request, template, context)


def tag_update(request, pk):
    template = "catalog/tag_update.html"
    tag = get_object_or_404(Tag, pk=pk)
    form = TagUpdateForm(request.POST or None)

    if form.is_valid():
        tag.slug = form.cleaned_data["slug"]
        tag.save(update_fields=["slug"])
    context = {
        "form": form,
    }
    return render(request, template, context)
'''
