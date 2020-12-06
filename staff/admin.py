from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, User

from mptt.admin import MPTTModelAdmin
from rest_framework.reverse import reverse
from django.utils.html import format_html

from .models import EmployeeMptt, InformationPaidSalary
from .forms import ProductModelInlineForm, UserChangeForm
from django_admin_relation_links import AdminChangeLinksMixin


class ProductModelInline(admin.StackedInline):
    model = EmployeeMptt
    form = ProductModelInlineForm
    extra = 1


class CustomUserAdmin(UserAdmin):
    inlines = (ProductModelInline, )
    form = UserChangeForm
    list_display = ('username', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'is_staff')
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
    list_display = ('full_name', 'role', 'parent_link', 'salary', 'total_paid',)
    list_filter = ('role', 'level')
    actions = ['delete_information']
    change_links = ['parent']
    fieldsets = (
        (None, {'fields': ('name', 'surname', 'middle_name', 'role',
                           'employment_date', 'salary', 'total_paid_list')
                }
         ),
    )
    readonly_fields = ['total_paid_list']

    @staticmethod
    def total_paid_list(obj):
        info_salary = InformationPaidSalary.objects.filter(employee=obj)
        if info_salary.count() == 0:
            return '0 $'
        info_list = []
        for info in info_salary:
            change_url = reverse('admin:staff_informationpaidsalary_change',
                                 args=(info.id, ))
            info_list.append('<a href="%s">%s</a>' % (change_url, info))
        return format_html(', '.join(info_list))

    def delete_information(self, request, queryset):
        for employee in queryset:
            info = InformationPaidSalary.objects.filter(employee=employee.id)
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
