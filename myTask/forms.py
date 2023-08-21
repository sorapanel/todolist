from django import forms
from django.utils import timezone

class TaskForm(forms.Form):
    name = forms.CharField(label='タスク名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='詳細', widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(label='開始日付', input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min':timezone.localdate(),}))
    start_time = forms.TimeField(label='開始時間', input_formats=['%H:%M'], widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'min':timezone.localtime(),}))
    finish_date = forms.DateField(label='終了日付', input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'min':timezone.localdate(),}))
    finish_time = forms.TimeField(label='終了時間', input_formats=['%H:%M'], widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'min':timezone.localtime(),}))
