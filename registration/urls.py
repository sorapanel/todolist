from django.urls import path
from . import views

from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

index = TemplateView.as_view(template_name = "index.html")

urlpatterns = [
    path('', index, name='index'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('signup', views.SignUpView.as_view(), name="signup"),
    path('logout/', login_required(views.Logout), name="logout"),
]
