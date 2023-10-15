from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import TaskModel
from .forms import TaskForm,TaskForm_Update
import datetime
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
def Main(request):

    user_name = request.session.get('username', None)

    contents = TaskModel.objects.filter(user_name=user_name['username'])

    tasks = []

    condition = True 

    if any(contents):
        condition = False


    for content in contents:
        if content.active:
            if not content.done:
                task_id = content.task_id
                name = content.name
                description = content.description
                start_date = content.start_date
                start_time = content.start_time
                finish_date = content.finish_date
                finish_time = content.finish_time

                tasks.append({
                    'task_id':task_id,
                    'name':name,
                    'description':description,
                    'start_date':start_date,
                    'start_time':start_time,
                    'finish_date':finish_date,
                    'finish_time':finish_time,
                })

    sorted_tasks = sorted(tasks, key=lambda x: x["start_time"])
    sorted_tasks = sorted(sorted_tasks, key=lambda x: x["start_date"])

    params = {
            'tasks':sorted_tasks,
            'condition':condition,
    }

    return render(request, 'myTask/main.html', params)



        

class FormView(TemplateView):
    template_name = 'myTask/addTask.html'
    form_class = TaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class()
        context['form'] = form
        context['message'] = ''
        return context
    
    def post(self, request):
        form = self.form_class(request.POST)
        current_time = datetime.datetime.now().time()
        current_time = current_time.replace(second=0, microsecond=0)
        current_date = datetime.date.today()
        print(current_date)
        print(current_time)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            start_time = form.cleaned_data['start_time']
            finish_date = form.cleaned_data['finish_date']
            finish_time = form.cleaned_data['finish_time']

            

            if start_date == current_date:
                if current_time > start_time:
                    message="現在日時より以前の時刻は選択できません。"
                    return render(request, "myTask/addTask.html", {'form': form, 'message':message})
            
            if finish_date == current_date:
                if current_time > finish_time:
                    message="現在日時より以前の時刻は選択できません。"
                    return render(request, "myTask/addTask.html", {'form': form, 'message':message})

            if start_time > finish_time:
                if start_date >= finish_date:
                    message="開始日時と終了日時に矛盾が生じています。"
                    return render(request, "myTask/addTask.html", {'form': form, 'message':message})
            
            if start_date > finish_date:
                    message="開始日時と終了日時に矛盾が生じています。"
                    return render(request, "myTask/addTask.html", {'form': form, 'message':message})
                
            user_name = request.session.get('username', None)
            if user_name is not None:
                TaskModel.objects.create(name=name, description=description, start_date=start_date, start_time=start_time, finish_date=finish_date, finish_time=finish_time, user_name=user_name['username'],)
                return redirect('main')
            else:
                message="もう一度ログインしなおしてください。"
                return render(request, "myTask/addTask.html", {'form': form, 'message':message})
        else:
            message="フォームが無効です。"
            return render(request, "myTask/addTask.html", {'form': form, 'message':message})
        
class Modify(UpdateView):
    template_name = "myTask/modTask.html"
    model = TaskModel
    form_class = TaskForm_Update
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            start_time = form.cleaned_data['start_time']
            finish_date = form.cleaned_data['finish_date']
            finish_time = form.cleaned_data['finish_time']
            if start_time > finish_time:
                if start_date >= finish_date:
                    message="開始日時と終了日時に矛盾が生じています。"
                    context = self.get_context_data()
                    context['form'] = form
                    context['message'] = message
                    return self.render_to_response(context)
            
            if start_date > finish_date:
                    message="開始日時と終了日時に矛盾が生じています。"
                    context = self.get_context_data()
                    context['form'] = form
                    context['message'] = message
                    return self.render_to_response(context)
            
            form.save()
            return super().form_valid(form)
        else:
            message = "フォーム内容が無効です。"
            context = self.get_context_data()
            context['form'] = form
            context['message'] = message
            return self.render_to_response(context)
        
def AllTask(request):

    user_name = request.session.get('username', None)

    contents = TaskModel.objects.filter(user_name=user_name['username'])

    tasks = []

    condition = True 

    if any(contents):
        condition = False

    for content in contents:
            task_id = content.task_id
            name = content.name
            description = content.description
            start_date = content.start_date
            start_time = content.start_time
            finish_date = content.finish_date
            finish_time = content.finish_time

            tasks.append({
                'task_id':task_id,
                'name':name,
                'description':description,
                'start_date':start_date,
                'start_time':start_time,
                'finish_date':finish_date,
                'finish_time':finish_time,
            })

    sorted_tasks = sorted(tasks, key=lambda x: x["start_time"])
    sorted_tasks = sorted(sorted_tasks, key=lambda x: x["start_date"])

    params = {
            'tasks':sorted_tasks,
            'condition':condition,
    }

    return render(request, 'myTask/allTask.html', params)


def Manage(request):

    username = request.session.get('username', None)
    if username is not None:
        task_count = 0
        done_count = 0
        contents = TaskModel.objects.filter(user_name=username['username'])

        for content in contents:
            task_count = task_count + 1
            if content.done:
                done_count = done_count + 1
        
        if task_count == 0:
            task_done = 0
        else:
            task_done = done_count/task_count

        params = {
            'username':username['username'],
            'task_count':task_count,
            'done_count':done_count,
            'task_done':task_done*100,
        }

        return render(request, "myTask/manage.html", params)
    
    else:
        return redirect('index')