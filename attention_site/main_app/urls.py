from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    path('main/', views.main_screen_yo, name='main_screen'),
    path('main/settings', views.settings, name='settings'),
    path('main/delete_item/<task_id>', views.delete_item, name='delete_item'),
]