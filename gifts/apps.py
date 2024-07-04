from django.apps import AppConfig


class GiftsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gifts"

    def ready(self):
        import gifts.signals
