from symbol import decorators
from urllib import request

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import django_filters
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from data.models import Data
from data.serializer import DataSerializer
from data.models import IllegalData
from data.serializer import IllegalDataSerializer
from data.models import TrafficFlow
from data.serializer import TrafficFlowSerializer
from data.models import IllegalStatistics
from data.serializer import IllegalStatisticsSerializer
# from data.models import SpeedLimit
# from data.serializer import SpeedLimitSerializer
from data.models import VideoSpeed
from data.serializer import VideoSerializer


# Create your views here.


# 数据测试
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('name', 'author')  # 列出搜索字段


# 违规信息
class IllegalDataViewSet(viewsets.ModelViewSet):
    queryset = IllegalData.objects.all()
    serializer_class = IllegalDataSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('id', 'videoId', 'plate', 'upload_time', 'illegal_time', 'illegal',)


# 路口饱和度
class TrafficFlowViewSet(viewsets.ModelViewSet):
    queryset = TrafficFlow.objects.all()
    serializer_class = TrafficFlowSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('videoId', 'car_number', 'motor_number', 'people_number',)


# 违规行为统计
class IllegalStatisticsViewSet(viewsets.ModelViewSet):
    queryset = IllegalStatistics.objects.all()
    serializer_class = IllegalStatisticsSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('videoId', 'value', 'name',)


# # 限速输入
# class SpeedLimitViewSet(viewsets.ModelViewSet):
#     queryset = SpeedLimit.objects.all()
#     serializer_class = SpeedLimitSerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     filter_fields = ('speed',)


# 视频路径
class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoSpeed.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('video_path', 'speed', )


    # def list(self, request, *args, **kwargs):
    #     video_path = request.query_params.get('video_path')		# 获取传过来的参数：参数（单参）解析
    #     print(video_path)
    #     speed = request.query_params.get('speed')
    #     print(speed)
    #     ser = self.get_serializer(self.queryset, many=True)
    #     self.serData = ser.data
    #     return Response(ser.data)
    # @decorators.list_route(methods=['post'])



@csrf_exempt
def my_api(request):
    dic = {}
    if request.method == 'GET':
        dic['message'] = 0
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = '方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))