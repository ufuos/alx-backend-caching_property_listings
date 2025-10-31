# properties/utils.py
from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Retrieve all Property objects with Redis caching.
    Cache expires after 1 hour (3600 seconds).
    """
    # 1️⃣ Check Redis for cached data
    properties = cache.get('all_properties')

    if properties is None:
        # 2️⃣ If not found, query the database
        print("Cache miss — fetching from database.")
        properties = list(Property.objects.all())  # convert queryset to list

        # 3️⃣ Store the result in Redis for 1 hour (3600 seconds)
        cache.set('all_properties', properties, timeout=3600)
    else:
        print("Cache hit — fetched from Redis.")

    # 4️⃣ Return the cached or freshly fetched data
    return properties
