from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from staff.api.serializers import EmployeeSerializerList, UserSerializer
from staff.models import EmployeeMptt
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view

from .permissions import ChiefPermissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@permission_classes([IsAuthenticated, ChiefPermissions])
class EmployeeListView(ReadOnlyModelViewSet):
    serializer_class = EmployeeSerializerList
    queryset = EmployeeMptt.objects.all()


class EmployeeListLevel0View(EmployeeListView):
    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=0)


class EmployeeListLevel1View(EmployeeListView):
    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=1)


class EmployeeListLevel2View(EmployeeListView):
    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=2)


class EmployeeListLevel3View(EmployeeListView):
    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=3)


class EmployeeListLevel4View(EmployeeListView):
    def get_queryset(self):
        return EmployeeListView.queryset.filter(level=4)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serialized_user = UserSerializer(user).data
    return Response({'user': serialized_user})
