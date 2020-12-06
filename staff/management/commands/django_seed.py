"""This module create custom command for creating users and group."""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User
from staff.models import EmployeeMptt
from staff.constants import EMPLOYEE_TYPES
from django_seed import Seed


def create_chief():
    seeder = Seed.seeder()
    seeder.add_entity(EmployeeMptt, 1, {
        'user': lambda x: User.objects.filter(employeemptt=None).first(),
        'role': lambda x: EMPLOYEE_TYPES['Chief_technical_officer'],
        'parent': lambda x: None,
        'level': 0,
    })
    seeder.execute()


def create_team():
    seeder1 = Seed.seeder()
    seeder1.add_entity(EmployeeMptt, 1, {
        'user': lambda x: User.objects.filter(employeemptt=None).first(),
        'role': lambda x: EMPLOYEE_TYPES['TeamLead'],
        'parent': lambda x: EmployeeMptt.objects.filter(role=EMPLOYEE_TYPES['Chief_technical_officer']).first(),
        'level': 1,
    })
    seeder1.execute()


def create_senior():
    seeder2 = Seed.seeder()
    seeder2.add_entity(EmployeeMptt, 1, {
        'user': lambda x: User.objects.filter(employeemptt=None).first(),
        'role': lambda x: EMPLOYEE_TYPES['Senior'],
        'parent': lambda x: EmployeeMptt.objects.filter(
            role=EMPLOYEE_TYPES['TeamLead']).first(),
        'level': 2,
    })
    seeder2.execute()


class Command(BaseCommand):
    """Create custom command."""

    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        create_chief()
        create_team()
        create_senior()
