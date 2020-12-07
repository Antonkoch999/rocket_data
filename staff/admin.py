"""This class is representation of User, Employee in the admin interface."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, User
from django.utils.html import format_html
from django.db.models import Sum

from mptt.admin import MPTTModelAdmin
from rest_framework.reverse import reverse
from django_admin_relation_links import AdminChangeLinksMixin

import staff.tasks
from staff.models import EmployeeMptt, InformationPaidSalary
from staff.forms import ProductModelInlineForm, UserChangeForm


class ProductModelInline(admin.StackedInline):
    """Allows inline model in User model."""

    model = EmployeeMptt
    form = ProductModelInlineForm
    extra = 1


class CustomUserAdmin(UserAdmin):
    """Class is representation of a model User in the admin interface."""

    inlines = (ProductModelInline, )
    form = UserChangeForm
    list_display = ('username', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name',
                           'is_staff')
                }
         ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', ),
        }),
    )


class AdminEmployeeMptt(AdminChangeLinksMixin, MPTTModelAdmin):
    """Class is representation of model EmployeeMptt in the admin interface."""

    list_display = ('full_name', 'role', 'parent_link', 'salary',
                    'total_paid',)
    list_filter = ('role', 'level')
    actions = ['delete_information']
    change_links = ['parent']
    fieldsets = (
        (None, {'fields': ('name', 'surname', 'patronymic', 'role',
                           'employment_date', 'salary', 'total_paid_list',
                           'parent', 'user')
                }
         ),
    )
    readonly_fields = ['total_paid_list']

    @staticmethod
    def total_paid(obj):
        """Show information about the sum of all payments."""
        total = InformationPaidSalary.objects.filter(
            employee=obj).aggregate(total_paid=Sum('salary'))['total_paid']
        if total is None:
            return '0 $'
        return f'{total} $'

    @staticmethod
    def total_paid_list(obj):
        """Show information about the number of salary payments."""
        info_salary = InformationPaidSalary.objects.select_related(
            'employee').filter(employee=obj)
        if info_salary.count() == 0:
            return '0 $'
        info_list = []
        for info in info_salary:
            change_url = reverse('admin:staff_informationpaidsalary_change',
                                 args=(info.id, ))
            info_list.append(f'<a href="{change_url}">{info}</a>')
        return format_html(', '.join(info_list))

    def delete_information(self, request, queryset):
        """Delete information.

        Removes all information about the number of salary payments, if
        the number of users is more than 20, then the task is sent to celery.
        """
        if queryset.count() > 20:
            lst = list(queryset.values_list('id', flat=True))
            staff.tasks.delete_task.delay(lst)
        else:
            for employee in queryset:
                info = InformationPaidSalary.objects.filter(
                    employee=employee.id)
                info.delete()


class GroupAdminWithCount(GroupAdmin):
    """Class is representation of a model Group in the admin interface."""

    list_display = GroupAdmin.list_display + ('user_count',)

    @staticmethod
    def user_count(obj):
        """Count the number of users in a group."""
        return obj.user_set.count()


class InformationPaidSalaryAdmin(admin.ModelAdmin):
    """Class is representation of InformationPaidSalary in admin interface."""

    list_display = ('employee', 'salary', 'data',)
    list_filter = ('employee', 'data')


admin.site.unregister(Group)
admin.site.register(Group, GroupAdminWithCount)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(EmployeeMptt, AdminEmployeeMptt)
admin.site.register(InformationPaidSalary, InformationPaidSalaryAdmin)
