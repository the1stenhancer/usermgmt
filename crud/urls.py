from django.urls import path
from . import views


app_name = 'crud'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]