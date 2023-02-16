from django.urls import path, re_path, register_converter
from . import converters, views


register_converter(converters.YearConverter, "yyyy")
register_converter(converters.PositiveNumberConverter, "pn")

urlpatterns = [
    path("", views.item_list),
    path("<int:pk>", views.item_detail),
    re_path(r"re/[1-9]\d*", views.new_page),
    path("<yyyy:year>/<pn:number>", views.converter),
]
