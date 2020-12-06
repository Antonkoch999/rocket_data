from __future__ import absolute_import, unicode_literals

from celery import shared_task
from staff.models import InformationPaidSalary, EmployeeMptt

import datetime


@shared_task
def payroll():
    users = EmployeeMptt.objects.all()
    for user in users:
        InformationPaidSalary.objects.create(
            employee=user,
            salary=int(user.salary),
            data=f"{datetime.datetime.now():%Y-%m-%d}",
        )


@shared_task
def delete_task(lst):
    for id_ in lst:
        info = InformationPaidSalary.objects.filter(employee=id_)
        info.delete()
