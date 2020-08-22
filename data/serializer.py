from rest_framework import serializers

from data.models import Data
from data.models import Video
from data.models import IllegalData
from data.models import TrafficFlow


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
        fields = ['car_number']
