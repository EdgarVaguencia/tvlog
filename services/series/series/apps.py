from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'series'

    def ready(self):
        import series.signals
