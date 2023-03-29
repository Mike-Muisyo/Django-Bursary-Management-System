from django.apps import AppConfig


class BursaryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bursary'

    def ready(self):
        import bursary.signals
