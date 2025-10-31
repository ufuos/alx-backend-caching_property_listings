# File: properties/apps.py
from django.apps import AppConfig


class PropertiesConfig(AppConfig):
default_auto_field = 'django.db.models.BigAutoField'
name = 'properties'


def ready(self):
# Import signals module to ensure signal handlers are registered when app is ready
# The import is inside ready() to avoid side-effects at import time.
from . import signals # noqa: F401




# File: properties/__init__.py
# For Django < 3.2, this ensures Django uses our AppConfig. For Django >= 3.2,
# apps are auto-discovered, but this line is harmless and satisfies the task
# instruction to update __init__.


default_app_config = 'properties.apps.PropertiesConfig'


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'
