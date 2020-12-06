"""This module create custom command for creating users and group."""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User
from staff.models import EmployeeMptt
from staff.constants import EMPLOYEE_TYPES
from django_seed import Seed


class Command(BaseCommand):
    """Create custom command."""

    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        seeder.add_entity(User, 5)
        seeder.execute()
