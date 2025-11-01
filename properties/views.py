
# properties/views.py
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property  # Ensure this model exists


# ✅ Cache this view for 15 minutes (60 * 15 seconds)
@cache_page(60 * 15)
def property_list(request):
    """
    Returns a JSON list of properties.
    Cached in Redis for 15 minutes via @cache_page.
    """
    # .values() returns dictionaries of model fields (so JsonResponse can serialize them).
    qs = Property.objects.all().values()
    data = list(qs)  # convert QuerySet of dicts to list
    return JsonResponse({
        "status": "success",
        "count": len(data),
        "properties": data
    })

