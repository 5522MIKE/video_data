from rest_framework import serializers

from data.models import Data
from data.models import Video
from data.models import IllegalData
from data.models import TrafficFlow
from data.models import IllegalStatistics
from data.models import SpeedLimit
from data.models import Video


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class IllegalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllegalData
        fields = '__all__'


class TrafficFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficFlow
        fields = ['car_number', 'motor_number', 'people_number', ]


class IllegalStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllegalStatistics
        fields = ['value', 'name', ]


class SpeedLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedLimit
        fields = ['speed', ]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_path', ]

