from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('main/', login_required(views.Main), name='main'),
    path('add_task/', login_required(views.FormView.as_view()), name='add_task'),
]
