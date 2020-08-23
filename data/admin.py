from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Data
from .models import IllegalData
from .models import TrafficFlow
from .models import IllegalStatistics
from .models import SpeedLimit
from .models import Video

admin.site.register(Data)
admin.site.register(IllegalData)
admin.site.register(TrafficFlow)
admin.site.register(IllegalStatistics)
admin.site.register(SpeedLimit)
admin.site.register(Video)