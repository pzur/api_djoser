from django.apps import AppConfig

class TablasConfig(AppConfig):
    name = 'tablas'

    def ready(self):
        import tablas.signals