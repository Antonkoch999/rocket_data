from rest_framework import serializers
from staff.models import EmployeeMptt


class EmployeeSerializerList(serializers.ModelSerializer):

    class Meta:
        model = EmployeeMptt
        fields = ['name', 'surname', 'middle_name', 'role', 'employment_date',
                  'salary', 'parent', 'total_paid', 'url']
        extra_kwargs = {
            'url': {
                'view_name': 'api:employeemptt-detail'
            },
        }


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeMptt
        fields = '__all__'
