from django.urls import path
from SampleAPI import SampleAPI_views

from mosega_backend.ConfigHandler import *
configs = ConfigHandler.load_config('config.yaml')


API_PATH = configs['api']['backend']['SampleAPI']['view'] + '/' +configs['api']['title'] + '/' +\
           configs['api']['current_version'] + '/' + configs['api']['backend']['SampleAPI']['name'] + '/'

urlpatterns = [
    path(API_PATH, SampleAPI_views.SampleAPIList.as_view()),
    path(API_PATH + '<int:pk>/', SampleAPI_views.SampleAPIDetails.as_view()),
]
