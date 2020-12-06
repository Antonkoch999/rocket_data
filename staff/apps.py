"""This class helps to include application configuration in settings."""

from django.apps import AppConfig


class StaffConfig(AppConfig):
    """Class representing a Staff application and its configuration."""

    name = 'staff'

    def ready(self):
        """At startup application imports signals."""
        import staff.signals
