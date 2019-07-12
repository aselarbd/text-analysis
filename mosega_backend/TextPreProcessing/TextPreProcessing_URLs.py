from django.urls import path
from TextPreProcessing import TextPreProcessing_views

from mosega_backend.ConfigHandler import *
configs = ConfigHandler.load_config('config.yaml')


API_PATH = configs['api']['backend']['TextPreProcessing']['view'] + '/' +configs['api']['title'] + '/' +\
           configs['api']['current_version'] + '/' + configs['api']['backend']['TextPreProcessing']['name'] + '/'

urlpatterns = [
    path(API_PATH, TextPreProcessing_views.TextPreProcessingList.as_view()),
    path(API_PATH + '<int:pk>/', TextPreProcessing_views.TextPreProcessingDetails.as_view()),
]
