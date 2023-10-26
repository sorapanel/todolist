from django.contrib import admin

# Register your models here.
from . models import TaskModel, LikeModel, CommentModel

admin.site.register(TaskModel)
admin.site.register(LikeModel)
admin.site.register(CommentModel)