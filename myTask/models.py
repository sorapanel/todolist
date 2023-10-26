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

class LikeModel(models.Model):
    is_like = models.BooleanField(null=False, default=False,)
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE, to_field="task_id",)
    user_name = models.CharField(null=False, max_length=100, blank=False,)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["task", "user_name"],
                name="like_unique"
            ),
        ]

class CommentModel(models.Model):
    comment_id = models.BigAutoField(primary_key=True,)
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE, to_field="task_id",)
    user_name = models.CharField(null=False, max_length=100, blank=False,)
    content = models.CharField(null=False, max_length=250, blank=True,)
    