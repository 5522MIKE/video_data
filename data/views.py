import django_filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from data.models import Data
from data.serializer import DataSerializer
from data.models import Video
from data.serializer import VideoSerializer
from data.models import IllegalData
from data.serializer import IllegalDataSerializer
from data.models import TrafficFlow
from data.serializer import TrafficFlowSerializer

# Create your views here.


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('name', 'author')  # 列出搜索字段


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class IllegalDataViewSet(viewsets.ModelViewSet):
    queryset = IllegalData.objects.all()
    serializer_class = IllegalDataSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('id', 'plate', 'upload_time', 'illegal_time', 'illegal',)


class TrafficFlowViewSet(viewsets.ModelViewSet):
    queryset = TrafficFlow.objects.all()
    serializer_class = TrafficFlowSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('car_number', )
