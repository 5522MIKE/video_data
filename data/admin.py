from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Data
from .models import IllegalData
from .models import TrafficFlow

admin.site.register(Data)
admin.site.register(IllegalData)
admin.site.register(TrafficFlow)