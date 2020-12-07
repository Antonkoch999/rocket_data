"""This module create custom command for creating users and group."""

import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from django_seed import Seed

from staff.models import EmployeeMptt


class Command(BaseCommand):
    """Create custom command."""

    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        seeder.add_entity(User, 20)

        seeder.add_entity(EmployeeMptt, 20, {
            'user': lambda x: User.objects.filter(employeemptt=None).first(),
            'parent': lambda x: EmployeeMptt.objects.order_by("?").first(),
            'level': lambda x: random.randint(0, 4),
        })
        seeder.execute()

