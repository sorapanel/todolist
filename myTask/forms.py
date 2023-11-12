from django import forms
from django.utils import timezone
from .models import TaskModel

#タスク登録用
class TaskForm(forms.Form):
    name = forms.CharField(label='タスク名', widget=forms.TextInput(attrs={'class': 'form-control'}))#タスク名
    description = forms.CharField(label='詳細', widget=forms.TextInput(attrs={'class': 'form-control'}))#詳細
    start_date = forms.DateField(label='開始日付', input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min':timezone.localdate(),}))#開始日付
    start_time = forms.TimeField(label='開始時間', input_formats=['%H:%M'], widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'min':timezone.localtime(),}))#開始時間
    finish_date = forms.DateField(label='終了日付', input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min':timezone.localdate(),}))#終了日付
    finish_time = forms.TimeField(label='終了時間', input_formats=['%H:%M'], widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'min':timezone.localtime(),}))#終了時間

#タスク更新用
class TaskForm_Update(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ("name","description","start_date","start_time","finish_date","finish_time","active","done")
        labels = {
            'name': 'タスク名',
            'description': '詳細',
            'start_date': '開始日付',
            'start_time': '開始時間',
            'finish_date': '終了日付',
            'finish_time': '終了時間',
            'active': '有効化',
            'done': '達成',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            "start_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            "start_time": forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', }),
            "finish_date": forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            "finish_time": forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', }),
            # "active": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # "done": forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
