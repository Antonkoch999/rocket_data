from django.conf import settings
from rest_framework.urls import path
from staff.api.views import (EmployeeListView, EmployeeListLevel0View, EmployeeListLevel1View, EmployeeListLevel2View, EmployeeListLevel3View, EmployeeListLevel4View)
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "api"

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('employee', EmployeeListView)
router.register('employee_level_0', EmployeeListLevel0View, basename="level-0")
router.register('employee_level_1', EmployeeListLevel1View, basename="level-1")
router.register('employee_level_2', EmployeeListLevel2View, basename="level-2")
router.register('employee_level_3', EmployeeListLevel3View, basename="level-3")
router.register('employee_level_4', EmployeeListLevel4View, basename="level-4")

urlpatterns = router.urls
# urlpatterns = [
#     path('employee/l0/', EmployeeListLevel0View.as_view({'get': 'list'}),
#          name='employee_level_0'),
    # path('employee/l1/', EmployeeListLevel1View.as_view(),
    #      name='employee_level_1'),
    # path('employee/l2/', EmployeeListLevel2View.as_view(),
    #      name='employee_level_2'),
    # path('employee/l3/', EmployeeListLevel3View.as_view(),
    #      name='employee_level_3'),
    # path('employee/l4/', EmployeeListLevel4View.as_view(),
    #      name='employee_level_4'),
# ]

