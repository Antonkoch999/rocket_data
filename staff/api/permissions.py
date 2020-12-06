"""This module contains custom permissions."""

from rest_framework import permissions
from staff.constants import EMPLOYEE_TYPES


class ChiefPermissions(permissions.BasePermission):
    """For users only with role Chief_technical_officer and superuser."""

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.groups.filter(
                name=EMPLOYEE_TYPES['Chief_technical_officer']).exists():
            return True
        return False
