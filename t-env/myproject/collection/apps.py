from django.apps import AppConfig


class CollectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'collection'


   # def ready(self):
       # import collection.signals  # Import the signals module
