from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import TaskModel
from .forms import TaskForm

# Create your views here.
def Main(request):

    contents = TaskModel.objects.all()

    tasks = []

    condition = True 

    if any(contents):
        condition = False


    for content in contents:
        name = content.name
        description = content.description
        start_date = content.start_date
        start_time = content.start_time
        finish_date = content.finish_date
        finish_time = content.finish_time

        tasks.append({
            'name':name,
            'description':description,
            'start_date':start_date,
            'start_time':start_time,
            'finish_date':finish_date,
            'finish_time':finish_time,
        })

    params = {
            'tasks':tasks,
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
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            start_time = form.cleaned_data['start_time']
            finish_date = form.cleaned_data['finish_date']
            finish_time = form.cleaned_data['finish_time']
            TaskModel.objects.create(name=name, description=description, start_date=start_date, start_time=start_time, finish_date=finish_date, finish_time=finish_time)
            return redirect('index')
        else:
            message="フォームが無効です。"
            return render(request, "myTask/addTask.html", {'form': form, 'message':message})

