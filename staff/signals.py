"""This module contains signals."""

from django.contrib.auth.models import Group
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from staff.models import EmployeeMptt
from staff.constants import EMPLOYEE_TYPES


@receiver(post_save, sender=User)
def my_user_handler(instance, created,  **kwargs):
    """Post-create user signal that adds the user is_staff equals True"""
    if created:
        instance.is_staff = True
        instance.save()


@receiver(pre_save, sender=EmployeeMptt)
def my_handler(instance,  **kwargs):
    """Pre-create EmployeeMptt signal that adds the user to everyone group."""

    try:
        if instance.role == EMPLOYEE_TYPES['Chief_technical_officer']:
            group = Group.objects.get(
                name=EMPLOYEE_TYPES['Chief_technical_officer'])
            instance.user.groups.add(group)
        elif instance.role == EMPLOYEE_TYPES['TeamLead']:
            group = Group.objects.get(name=EMPLOYEE_TYPES['TeamLead'])
            instance.user.groups.add(group)
        elif instance.role == EMPLOYEE_TYPES['Senior']:
            group = Group.objects.get(name=EMPLOYEE_TYPES['Senior'])
            instance.user.groups.add(group)
        elif instance.role == EMPLOYEE_TYPES['Middle']:
            group = Group.objects.get(name=EMPLOYEE_TYPES['Middle'])
            instance.user.groups.add(group)
        elif instance.role == EMPLOYEE_TYPES['Junior']:
            group = Group.objects.get(name=EMPLOYEE_TYPES['Junior'])
            instance.user.groups.add(group)

    except Group.DoesNotExist:
        print('Group.DoesNotExist')
