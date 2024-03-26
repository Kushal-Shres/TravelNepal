"""travelnepal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from travelnepal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travel.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('search.urls'), name='search'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('travel/', include('travel.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('web/adventures', TemplateView.as_view(template_name='web/adventures.html'), name='home'),
    path('web/religious', TemplateView.as_view(template_name='web/religious.html'), name='home'),
    path('web/trekking', TemplateView.as_view(template_name='web/trekking.html'), name='home'),
    path('web/places', TemplateView.as_view(template_name='web/places.html'), name='home'),


    # path('accounts/', include('accounts.urls')),
    # url(r'^$', views.login_redirect, name='login_redirect'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
