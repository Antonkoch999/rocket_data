"""This module contents view methods for EmployeeMptt."""

from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from staff.api.serializers import EmployeeSerializerList, UserSerializer
from staff.api.permissions import ChiefPermissions
from staff.models import EmployeeMptt


@permission_classes([IsAuthenticated, ChiefPermissions])
class EmployeeListView(ReadOnlyModelViewSet):
    """List, retrieve views of EmployeeMptt."""

    serializer_class = EmployeeSerializerList
    queryset = EmployeeMptt.objects.all()


class EmployeeListLevel0View(EmployeeListView):
    """List views of EmployeeMptt with level 0."""

    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=0)


class EmployeeListLevel1View(EmployeeListView):
    """List views of EmployeeMptt with level 1."""

    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=1)


class EmployeeListLevel2View(EmployeeListView):
    """List views of EmployeeMptt with level 2."""

    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=2)


class EmployeeListLevel3View(EmployeeListView):
    """List views of EmployeeMptt with level 3."""

    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=3)


class EmployeeListLevel4View(EmployeeListView):
    """List views of EmployeeMptt with level 4."""

    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=4)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    """View for request user."""
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user})
