"""mosega_backend URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from mosega_backend.ConfigHandler import *
configs = ConfigHandler.load_config('config.yaml')


# Get a default view for SWAGGER
schema_view = get_swagger_view(title='Backend Swagger API')

Swagger_Path = configs['api']['title'] + '/' + configs['api']['current_version'] + '/' +\
               configs['api']['documentation'] + '/'

urlpatterns = [
    path(Swagger_Path, schema_view),

    path('', include('SampleAPI.SampleAPI_URLs')),

    path('api/v1/textProcessing/', include('TextPreProcessing.TextPreProcessing_URLs')),

    path('admin/', admin.site.urls),
]
