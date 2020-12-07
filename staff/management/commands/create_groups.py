"""This module create custom command for creating users and group."""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User
from staff.models import EmployeeMptt
from staff.constants import EMPLOYEE_TYPES


class Command(BaseCommand):
    """Create custom command."""

    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        """Logic custom command.

        Create users and groups and appoints permissions for groups.
        """
        first_element_tuple = 0
        groups = {'Chief_technical_officer': None, 'TeamLead': None,
                  'Senior': None, 'Middle': None, 'Junior': None}

        for group in groups:
            groups[group] = Group.objects.get_or_create(name=group)[
                first_element_tuple]
            groups[group].save()

        users = {'Chief_technical_officer': None, 'TeamLead': None,
                 'Senior': None, 'Middle': None, 'Junior': None}

        for user in users:
            users[user] = User.objects.get_or_create(
                username=user)[first_element_tuple]
            users[user].set_password('12345')
            users[user].save()

        chief_technical_officer_employee = EmployeeMptt.objects.get_or_create(
                user=users['Chief_technical_officer'],
                role=EMPLOYEE_TYPES['Chief_technical_officer'],
                name='Petr', surname='Ivanov', middle_name='Stepanovich',
                employment_date='2020-08-10', salary=3000,
            )[first_element_tuple]
        chief_technical_officer_employee.save()

        team_lead_employee = EmployeeMptt.objects.get_or_create(
                user=users['TeamLead'],
                role=EMPLOYEE_TYPES['TeamLead'],
                name='Artem', surname='Babitski', middle_name='Aleksandovich',
                employment_date='2020-08-10', salary=2500,
            )[first_element_tuple]
        team_lead_employee.save()
        chief_technical_officer_employee.employee.add(team_lead_employee)

        senior_employee = EmployeeMptt.objects.get_or_create(
                user=users['Senior'],
                role=EMPLOYEE_TYPES['Senior'],
                name='Andrey', surname='Palmdropov', middle_name='Antonovich',
                employment_date='2020-08-10', salary=2000,
            )[first_element_tuple]
        senior_employee.save()
        team_lead_employee.employee.add(senior_employee)

        middle_employee = EmployeeMptt.objects.get_or_create(
            user=users['Middle'],
            role=EMPLOYEE_TYPES['Middle'],
            name='Sasha', surname='Petrov', middle_name='Alekseevich',
            employment_date='2020-08-10', salary=1500,
        )[first_element_tuple]
        middle_employee.save()
        senior_employee.employee.add(middle_employee)

        junior_employee = EmployeeMptt.objects.get_or_create(
            user=users['Junior'],
            role=EMPLOYEE_TYPES['Junior'],
            name='Anton', surname='Kochnevsky', middle_name='Pavlovich',
            employment_date='2020-08-10', salary=1000,
        )[first_element_tuple]
        junior_employee.save()
        middle_employee.employee.add(junior_employee)

        permissions_list = (
            'Can add user', 'Can change user', 'Can view user',
            'Can delete user',
        )

        permission_chief = Permission.objects.filter(
            name__in=permissions_list)
        permission_team_lead = Permission.objects.filter(
            name__in=permissions_list)
        permission_senior = Permission.objects.filter(
            name__in=permissions_list)
        permissions_middle = Permission.objects.filter(
            name__in=permissions_list)
        permissions_junior = Permission.objects.filter(
            name__in=permissions_list)

        groups['Chief_technical_officer'].permissions.add(*permission_chief)
        groups['TeamLead'].permissions.add(*permission_team_lead)
        groups['Senior'].permissions.add(*permission_senior)
        groups['Middle'].permissions.add(*permissions_middle)
        groups['Junior'].permissions.add(*permissions_junior)

        groups['Chief_technical_officer'].save()
        groups['TeamLead'].save()
        groups['Senior'].save()
        groups['Middle'].save()
        groups['Junior'].save()

        users['Chief_technical_officer'].save()
        users['TeamLead'].save()
        users['Senior'].save()
        users['Middle'].save()
        users['Junior'].save()

        chief_technical_officer_employee.save()
        team_lead_employee.save()
        senior_employee.save()
        middle_employee.save()
        junior_employee.save()
