from django.urls import path
from catalog import views

app_name = "catalog"

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:pk>/", views.item_detail, name="item_detail"),
    #path("tag_create/", views.tag_create, name="tag_create"),
    #path("tag_delete/<int:pk>/", views.tag_delete, name="tag_delete"),
    #path("tag_update/<int:pk>/", views.tag_update, name="tag_update"),
]
