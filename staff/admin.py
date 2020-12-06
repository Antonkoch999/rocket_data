"""This class is representation of User, Employee in the admin interface."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, User
from django.utils.html import format_html

from mptt.admin import MPTTModelAdmin
from rest_framework.reverse import reverse
from django_admin_relation_links import AdminChangeLinksMixin

from staff.models import EmployeeMptt, InformationPaidSalary
from staff.forms import ProductModelInlineForm, UserChangeForm
from staff.tasks import delete_task


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
    def total_paid_list(obj):
        """Show information about the number of salary payments."""
        info_salary = InformationPaidSalary.objects.filter(employee=obj)
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
            lst = []
            for employee in queryset:
                lst.append(employee.id)
            delete_task.delay(lst)
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


admin.site.unregister(Group)
admin.site.register(Group, GroupAdminWithCount)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(EmployeeMptt, AdminEmployeeMptt)
admin.site.register(InformationPaidSalary)
