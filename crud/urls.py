from django.urls import path
from . import views


app_name = 'crud'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('login?next=<str:next>', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]