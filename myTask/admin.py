from django.contrib import admin

# Register your models here.
from . models import TaskModel, LikeModel

admin.site.register(TaskModel)
admin.site.register(LikeModel)