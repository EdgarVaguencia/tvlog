from django.apps import AppConfig

class ApiConfig(AppConfig):
    name = 'temporadas'

    def ready(self):
        import temporadas.signals
