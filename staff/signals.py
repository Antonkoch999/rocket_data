"""This module contains signals."""

from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import EmployeeMptt
from django.contrib.auth.models import User
from .constants import EMPLOYEE_TYPES


@receiver(post_save, sender=User)
def my_user_handler(instance, created,  **kwargs):
    """Post-create user signal that adds the user to everyone group."""

    if created:
        instance.is_staff = True
        instance.save()


@receiver(post_save, sender=EmployeeMptt)
def my_handler(instance, created,  **kwargs):
    """Post-create user signal that adds the user to everyone group."""

    if created:
        try:
            if instance.role == EMPLOYEE_TYPES['Chief_technical_officer']:
                group = Group.objects.get(name=EMPLOYEE_TYPES['Chief_technical_officer'])
                instance.save()
                instance.user.groups.add(group)
            elif instance.role == EMPLOYEE_TYPES['TeamLead']:
                group = Group.objects.get(name=EMPLOYEE_TYPES['TeamLead'])
                instance.save()
                instance.user.groups.add(group)
            elif instance.role == EMPLOYEE_TYPES['Senior']:
                group = Group.objects.get(name=EMPLOYEE_TYPES['Senior'])
                instance.save()
                instance.user.groups.add(group)
            elif instance.role == EMPLOYEE_TYPES['Middle']:
                group = Group.objects.get(name=EMPLOYEE_TYPES['Middle'])
                instance.save()
                instance.user.groups.add(group)
            elif instance.role == EMPLOYEE_TYPES['Junior']:
                group = Group.objects.get(name=EMPLOYEE_TYPES['Junior'])
                instance.save()
                instance.user.groups.add(group)

        except Group.DoesNotExist:
            print('Group.DoesNotExist')
