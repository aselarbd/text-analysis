from django.urls import path

from ProcessingAPI.views import Processing
from Handlers.Config.ConfigHandler import *
configs = ConfigHandler.load_config('config.yaml')


API_PATH = configs['api']['backend']['Processing']['view'] + '/' +configs['api']['title'] + '/' +\
           configs['api']['current_version'] + '/' + configs['api']['backend']['Processing']['name'] + '/'

urlpatterns = [
    path(API_PATH, Processing.as_view()),
]
