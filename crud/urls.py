from django.urls import path
from . import views


app_name = 'crud'

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login?next=<str:next>', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('references', views.references, name='references'),
    path('users', views.users, name="users"),
    path('update?id=<int:pk>', views.update_user, name="update"),
    path('delete?id=<int:pk>', views.delete_user, name='delete'),
]