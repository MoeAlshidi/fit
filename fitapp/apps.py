from django.apps import AppConfig


class FitappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fitapp'
    
    def ready(self) -> None:
        import fitapp.signals
