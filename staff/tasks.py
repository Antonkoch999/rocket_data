"""This module is used to create tasks Celery."""

from __future__ import absolute_import, unicode_literals
import datetime

from celery import shared_task

from staff.models import InformationPaidSalary, EmployeeMptt


@shared_task
def payroll():
    """Every 2 hours credits to the employee wages."""
    users = EmployeeMptt.objects.all()
    for user in users:
        InformationPaidSalary.objects.create(
            employee=user,
            salary=int(user.salary),
            data=f"{datetime.datetime.now():%Y-%m-%d}",
        )


@shared_task
def delete_task(lst):
    """Removes all information about the number of salary payments.

    The list(lst) contains id EmployeeMptt.
    """
    for id_ in lst:
        info = InformationPaidSalary.objects.filter(employee=id_)
        info.delete()
