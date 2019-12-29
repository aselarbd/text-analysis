from django.urls import path

from ProcessingAPI.views import ProcessingOne
from Handlers.Config.ConfigHandler import *
configs = ConfigHandler.load_config('config.yaml')


API_PATH = configs['api']['backend']['Processing']['view'] + '/' +configs['api']['title'] + '/' +\
           configs['api']['current_version'] + '/' + configs['api']['backend']['Processing']['name'] + '/'

urlpatterns = [
    path(API_PATH, ProcessingOne.as_view()),
]
