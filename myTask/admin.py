from django.contrib import admin

# Register your models here.
from . models import TaskModel

admin.site.register(TaskModel)