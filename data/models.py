from django.db import models


# Create your models here.

# 数据测试表
class Data(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)


# 违规信息表
class IllegalData(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=30)
    upload_time = models.CharField(max_length=30)
    illegal_time = models.CharField(max_length=30)
    illegal = models.CharField(max_length=30)
    img = models.CharField(max_length=70)


# 路口车流量统计表
class TrafficFlow(models.Model):
    id = models.IntegerField(primary_key=True)
    # video = models.ForeignKey('Video', on_delete=models.CASCADE)
    car_number = models.IntegerField()
    motor_number = models.IntegerField()
    people_number = models.IntegerField()


# 违规行为统计表
class IllegalStatistics(models.Model):
    id = models.IntegerField(primary_key=True)
    # video = models.ForeignKey('Video', on_delete=models.CASCADE)
    value = models.IntegerField()
    name = models.CharField(max_length=10)


# # 限速表
# class SpeedLimit(models.Model):
#     id = models.IntegerField(primary_key=True)
#     # video = models.ForeignKey('Video', on_delete=models.CASCADE)
#     speed = models.IntegerField()


# 视频Video表
class VideoSpeed(models.Model):
    id = models.IntegerField(primary_key=True)
    upload_time = models.CharField(max_length=100)
    video_path = models.CharField(max_length=100)
    speed = models.IntegerField()