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
    filter_fields = ('video_path', 'speed', 'id', )


    # def list(self, request, *args, **kwargs):
    #     video_path = request.query_params.get('video_path')		# 获取传过来的参数：参数（单参）解析
    #     print(video_path)
    #     speed = request.query_params.get('speed')
    #     print(speed)
    #     ser = self.get_serializer(self.queryset, many=True)
    #     self.serData = ser.data
    #     return Response(ser.data)
    # @decorators.list_route(methods=['post'])


class VideoYoloViewSet(viewsets.ModelViewSet):
    queryset = VideoSpeed.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('video_path', 'speed', 'id', )

    def list(self, request, *args, **kwargs):
        video_path = request.query_params.get('video_path')  # 获取传过来的参数：参数（单参）解析
        queryset = VideoSpeed.objects.all()
        print(video_path)
        data = {}
        for title in queryset:
            data[title.id] = title.video_path
        return HttpResponse(json.dumps("1", ensure_ascii=False))
        # return HttpResponse(json.dumps(data, ensure_ascii=False))
        # return HttpResponse(queryset)



@csrf_exempt
def volo(request):
    dic = {}
    if request.method == 'GET':
        ID = request.GET.get('id', default='110')
        print(ID)
        dic['message'] = 0
        return HttpResponse(json.dumps(dic))
    else:
        dic['message'] = '方法错误'
        return HttpResponse(json.dumps(dic, ensure_ascii=False))

    # if request.method == "POST":
    #     req = json.loads(request.body)
    #     print(req)
    #     key_flag = req.get("title") and req.get("content") and len(req) == 2
    #     # 判断请求体是否正确
    #     if key_flag:
    #         title = req["title"]
    #         content = req["content"]
    #         # title返回的是一个list
    #         title_exist = Article.objects.filter(title=title)
    #         # 判断是否存在同名title
    #         if len(title_exist) != 0:
    #             return JsonResponse({"status": "BS.400", "msg": "title aleady exist,fail to publish."})
    #
    #         '''插入数据'''
    #         add_art = Article(title=title, content=content, status="alive")
    #         add_art.save()
    #         return JsonResponse({"status": "BS.200", "msg": "publish article sucess."})
    #     else:
    #         return JsonResponse({"status": "BS.400", "message": "please check param."})
    #
    # if request.method == "GET":
    #     articles = {}
    #     query_art = VideoSpeed.objects.all()
    #     for title in query_art:
    #         articles[title.title] = title.status
    #     return JsonResponse({"status":"BS.200","all_titles":articles,"msg":"query articles sucess."})