"""This class helps to include application configuration in settings."""

from django.apps import AppConfig


class StaffConfig(AppConfig):
    """Class representing a Staff application and its configuration."""

    name = 'staff'

    def ready(self):
        import staff.signals
