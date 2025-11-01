# alx_backend_caching_property_listings/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("properties/", include("properties.urls")),  # <-- routes /properties/ to property_list
]

