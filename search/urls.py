from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from search import views
from django.urls import reverse


urlpatterns = [
     # path('search/', searchposts),
    path('search/', views.searchposts, name='search'),


]
