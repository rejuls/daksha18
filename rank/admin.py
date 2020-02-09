from django.contrib import admin
from .models import Point,OnstageResult,OffstageResult


# Register your models here.
admin.site.register(Point)
admin.site.register(OnstageResult)
admin.site.register(OffstageResult)
