from django.apps import AppConfig


class FlowbackAiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flowback_addon.flowback_ai'
    def ready(self) -> None:
        from . import signals
        return super().ready()
