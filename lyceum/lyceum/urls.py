from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("catalog/<int:pk>", include("catalog.urls")),
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar

    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
