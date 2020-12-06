"""This module creates tables in the database."""

from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from rest_framework.reverse import reverse

from staff.constants import EMPLOYEE_TYPES


class EmployeeMptt(MPTTModel):
    """This class creates EmployeeMptt table.

    Here is used django-mptt, it creates a hierarchy.
    """

    EMPLOYEE_TYPES = tuple(EMPLOYEE_TYPES.items())
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES,
                            null=True, blank=True)
    name = models.CharField(max_length=35, null=True, blank=True)
    surname = models.CharField(max_length=35, null=True, blank=True)
    patronymic = models.CharField(max_length=35, null=True, blank=True)
    employment_date = models.DateField(null=True, blank=True)
    salary = models.PositiveSmallIntegerField(verbose_name='Salary in $',
                                              null=True, blank=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='employee')

    class Meta:
        """Metadata of EmployeeMptt."""

        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self) -> str:
        """Return the string representation of the object.

        :return: example: Name Surname - Role
        """
        return f'{self.name} {self.surname} - {self.role}'

    def full_name(self) -> str:
        """Return the string with fullname user.

        :return: example: Surname Name Patronymic
        """
        return f'{self.surname} {self.name} {self.patronymic}'

    def total_paid(self) -> str:
        """Calculate the amount of paid salary.

        :return: example: '1234 $'
        """
        total = InformationPaidSalary.objects.filter(employee=self.pk)
        if total.aggregate(total=models.Sum("salary"))["total"] is None:
            return '0 $'
        return f'{total.aggregate(total=models.Sum("salary"))["total"]} $'

    def get_absolute_url(self) -> str:
        """Get url for user's detail view.

        :return: URL for user detail.
        """
        return reverse("api:employeemptt-detail", kwargs={"pk": self.pk})


class InformationPaidSalary(models.Model):
    """This class creates InformationPaidSalary table."""

    employee = models.ForeignKey(EmployeeMptt, on_delete=models.CASCADE)
    data = models.DateField()
    salary = models.IntegerField()

    def __str__(self) -> str:
        """Return the string representation of the object.

        :return: example: Name Surname - Role/2020-10-10/1234
        """
        return f'{self.employee}/{self.data}/{self.salary}'
