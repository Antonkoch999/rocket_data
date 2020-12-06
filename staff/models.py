from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from .constants import EMPLOYEE_TYPES
from rest_framework.reverse import reverse


class EmployeeMptt(MPTTModel):

    EMPLOYEE_TYPES = tuple(EMPLOYEE_TYPES.items())
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
                            blank=True)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES, null=True,
                            blank=True)
    name = models.CharField(max_length=35, null=True,
                            blank=True)
    surname = models.CharField(max_length=35, null=True,
                            blank=True)
    middle_name = models.CharField(max_length=35, null=True,
                            blank=True)
    employment_date = models.DateField(null=True,
                            blank=True)
    salary = models.PositiveSmallIntegerField(verbose_name='Salary in $', null=True,
                            blank=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='employee')

    def __str__(self):
        return f'{self.name} {self.surname} - {self.role}'

    def full_name(self):
        return f'{self.surname} {self.name} {self.middle_name}'

    def total_paid(self):
        total = InformationPaidSalary.objects.filter(employee=self.pk)
        if total.aggregate(total=models.Sum("salary"))["total"] is None:
            return f'0 $'
        return f'{total.aggregate(total=models.Sum("salary"))["total"]} $'

    def get_absolute_url(self) -> str:
        """"Get url for user's detail view.
        :return: URL for user detail.
        """
        return reverse("api:employeemptt-detail", kwargs={"pk": self.pk})


class InformationPaidSalary(models.Model):
    employee = models.ForeignKey(EmployeeMptt, on_delete=models.CASCADE)
    data = models.DateField()
    salary = models.IntegerField()

    def __str__(self):
        return f'{self.employee} {self.data} {self.salary}'
