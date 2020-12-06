"""EmployeeMptt classes serializers for api."""

from rest_framework import serializers
from staff.models import EmployeeMptt


class EmployeeSerializerList(serializers.ModelSerializer):
    """Serializing EmployeeMptt instance for api views."""

    class Meta:
        """Metadata of EmployeeMptt."""

        model = EmployeeMptt
        fields = ['name', 'surname', 'middle_name', 'role', 'employment_date',
                  'salary', 'parent', 'total_paid', 'url']
        extra_kwargs = {
            'url': {
                'view_name': 'api:employeemptt-detail'
            },
        }


class UserSerializer(serializers.ModelSerializer):
    """Serializing EmployeeMptt for request user instance for api views."""

    class Meta:
        """Metadata of EmployeeMptt."""

        model = EmployeeMptt
        fields = '__all__'
