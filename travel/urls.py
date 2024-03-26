
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib import admin
from travel import views

app_name = 'travel'

urlpatterns = [
    # path('', views.index, name='index'),
    path('web/place', views.place_list, name='place'),
    path('register/', views.user_register, name='user_register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),


]


