"""This module displays URL patterns."""

from django.conf import settings
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from staff.api.views import (
    EmployeeListView, EmployeeListLevel0View, EmployeeListLevel1View,
    EmployeeListLevel2View, EmployeeListLevel3View, EmployeeListLevel4View,
    profile)

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


urlpatterns = [
    path('profile/', profile, name='profile'),
]

urlpatterns += router.urls
