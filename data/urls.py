from django.urls import path, include
from rest_framework.routers import DefaultRouter

from data import views


router = DefaultRouter()
router.register('data', views.DataViewSet)
router.register('video', views.VideoViewSet)
router.register('IllegalData', views.IllegalDataViewSet)
router.register('TrafficFlow', views.TrafficFlowViewSet)
router.register('IllegalStatistics', views.IllegalStatisticsViewSet)
router.register('SpeedLimit', views.SpeedLimitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]