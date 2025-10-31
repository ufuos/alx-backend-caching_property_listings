# properties/urls.py
from django.urls import path
from .views import property_list

app_name = "properties"

urlpatterns = [
    # maps /properties/ to the view (we will include this in the project urls)
    path("", property_list, name="property_list"),
]
