from django.urls import path, re_path, register_converter
from catalog import converters, views

app_name = "catalog"

register_converter(converters.DogOrFogConverter, "df")
register_converter(converters.PositiveNumberConverter, "pn")

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:pk>", views.item_detail, name="item_detail"),
    re_path(r"re/[1-9]\d*", views.new_page),
    path(
        "<df:text>/<pn:number>",
        views.converter,
        name="catalog-item-pos-int-name",
    ),
]
