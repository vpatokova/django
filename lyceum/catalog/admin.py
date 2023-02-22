from django.contrib import admin

import catalog.models


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.id.field.name,
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.name.field.name,
        catalog.models.Item.text.field.name,
    )
    list_editable = ("is_published",)
    list_display_links = ("name",)
    list_display = (
        "name",
        "is_published",
    )


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Tag.id.field.name,
        catalog.models.Tag.name.field.name,
        catalog.models.Tag.is_published.field.name,
        catalog.models.Tag.slug.field.name,
    )
    list_display_links = ("name",)
    list_display = (
        "id",
        "name",
    )


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Category.is_published.field.name,
        catalog.models.Category.id.field.name,
        catalog.models.Category.name.field.name,
        catalog.models.Category.slug.field.name,
        catalog.models.Category.weight.field.name,
    )
    list_display_links = ("name",)
    list_display = (
        "id",
        "name",
    )
