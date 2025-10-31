# File: properties/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache


# Import the Property model here. Importing at top-level is fine as long as
# there are no circular imports in your project. If you run into circular
# import errors, move the import inside the receiver functions.
from .models import Property


@receiver(post_save, sender=Property)
def invalidate_all_properties_cache_on_save(sender, instance, **kwargs):
"""Invalidate the 'all_properties' cache key after a Property is created or updated."""
cache.delete('all_properties')


@receiver(post_delete, sender=Property)
def invalidate_all_properties_cache_on_delete(sender, instance, **kwargs):
"""Invalidate the 'all_properties' cache key after a Property is deleted."""
cache.delete('all_properties')

