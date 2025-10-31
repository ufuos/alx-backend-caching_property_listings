
import logging
from django_redis import get_redis_connection
from django.core.cache import cache
from .models import Property

# Initialize logger at the top of the file
logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Retrieve Redis cache metrics: hits, misses, and hit ratio.
    """
    try:
        # Step 1: Connect to Redis using django_redis
        redis_conn = get_redis_connection("default")

        # Step 2: Get cache info from Redis
        info = redis_conn.info()

        # Step 3: Extract hits and misses
        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)

        # Step 4: Calculate the hit ratio
        total_requests = hits + misses
        hit_ratio = (hits / total_requests) if total_requests > 0 else 0.0

        # Step 5: Log the metrics
        logger.info(
            f"Redis Cache Metrics -> Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}"
        )

        # Step 6: Return the results as a dictionary
        return {
            "hits": hits,
            "misses": misses,
            "hit_ratio": round(hit_ratio, 2)
        }

    except Exception as e:
        # ✅ Required: Log any errors that occur
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {
            "hits": 0,
            "misses": 0,
            "hit_ratio": 0.0
        }


def get_all_properties():
    """
    Retrieve all Property objects with Redis caching.
    Cache expires after 1 hour (3600 seconds).
    """
    # 1️⃣ Check Redis for cached data
    properties = cache.get('all_properties')

    if properties is None:
        # 2️⃣ If not found, query the database
        logger.info("Cache miss — fetching from database.")
        properties = list(Property.objects.all())  # convert queryset to list

        # 3️⃣ Store the result in Redis for 1 hour (3600 seconds)
        cache.set('all_properties', properties, timeout=3600)
    else:
        logger.info("Cache hit — fetched from Redis.")

    # 4️⃣ Return the cached or freshly fetched data
    return properties
