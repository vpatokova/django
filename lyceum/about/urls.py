from django.urls import path
from . import views


urlpatterns = [path("about/", views.item_description)]
