from django.apps import AppConfig
import properties.signals  # ✅ required import


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    def ready(self):
        import properties.signals  # ✅ ensures signals are registered

