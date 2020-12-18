import Initialization
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from Handlers.Config.ConfigHandler import *
configs = ConfigHandler.load_config('config.yaml')


# Get a default view for SWAGGER
schema_view = get_swagger_view(title='Backend Swagger API')

Swagger_Path = configs['api']['title'] + '/' + configs['api']['current_version'] + '/' +\
               configs['api']['documentation'] + '/'

urlpatterns = [
    path(Swagger_Path, schema_view),

    path('', include('PrivacyPolicy.urls')),

    path('', include('TermsAndConditions.urls')),

    path('', include('ProcessingAPI.urls')),

    path('admin/', admin.site.urls),
]

Initialization.initialization()
