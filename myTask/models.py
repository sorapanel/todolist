from django.db import models

# Create your models here.
#タスク用
class TaskModel(models.Model):
    task_id = models.BigAutoField(primary_key=True,)#タスクID
    name = models.CharField(null=False, max_length=100, blank=False,)#タスク名
    user_name = models.CharField(null=False, max_length=100, blank=False,)#氏名
    description = models.CharField(null=True, blank=True, max_length=250,)#詳細
    start_date = models.DateField()#開始日付
    start_time = models.TimeField()#開始時間
    finish_date = models.DateField()#終了日付
    finish_time = models.TimeField()#終了日時
    like = models.IntegerField(null=False,blank=False,default=0,)#いいね数
    active = models.BooleanField(null=False, default=True)#有効化
    done = models.BooleanField(null=False, default=False,)#達成済みかどうか

#いいねに関するモデル
class LikeModel(models.Model):
    is_like = models.BooleanField(null=False, default=False,)#いいねされたかどうか
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE, to_field="task_id",)#タスクの外部キー
    user_name = models.CharField(null=False, max_length=100, blank=False,)#ユーザネーム

    class Meta:#タスクとユーザ名の複合主キー
        constraints = [
            models.UniqueConstraint(
                fields=["task", "user_name"],
                name="like_unique"
            ),
        ]
#コメントに関するモデル
class CommentModel(models.Model):
    comment_id = models.BigAutoField(primary_key=True,)#コメントID
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE, to_field="task_id",)#タスクの外部キー
    user_name = models.CharField(null=False, max_length=100, blank=False,)#ユーザ名
    content = models.CharField(null=False, max_length=250, blank=True,)#コメント内容
    
