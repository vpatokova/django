from django.contrib import admin
import catalog.models


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Tag.id.field.name,
        catalog.models.Tag.name.field.name,
    )
    list_display_links = ("name",)


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Category.id.field.name,
        catalog.models.Category.name.field.name,
    )
    list_display_links = ("name",)


class ImageInline(admin.TabularInline):
    model = catalog.models.Image
    extra = 0


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        catalog.models.Item.is_published.field.name,
        catalog.models.Item.name.field.name,
        catalog.models.Item.image_tmb,
    )
    list_editable = ("is_published",)
    list_display_links = ("name",)
    inlines = [
        ImageInline,
    ]
