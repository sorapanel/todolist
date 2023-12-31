from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('main/', login_required(views.Main), name='main'),
    path('add_task/', login_required(views.FormView.as_view()), name='add_task'),
    path('mod_task/<int:pk>', login_required(views.Modify.as_view()), name = "mod_task"),
    path('all_task/', login_required(views.AllTask), name = "all_task"),
    path('manage/', login_required(views.Manage), name="manage"),
    path('online_task/', login_required(views.OnlineTask), name="online_task"),
]
