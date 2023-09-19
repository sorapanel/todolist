from django.db import models

# Create your models here.
class TaskModel(models.Model):
    task_id = models.BigAutoField(primary_key=True,)
    name = models.CharField(null=False, max_length=100, blank=False,)
    user_name = models.CharField(null=False, max_length=100, blank=False,)
    description = models.CharField(null=True, blank=True, max_length=250,)
    start_date = models.DateField()
    start_time = models.TimeField()
    finish_date = models.DateField()
    finish_time = models.TimeField()
    like = models.IntegerField(null=False,blank=False,default=0,)
    active = models.BooleanField(null=False, default=True)
    done = models.BooleanField(null=False, default=False,)