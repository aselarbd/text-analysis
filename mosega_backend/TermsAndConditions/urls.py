from django.urls import path

from TermsAndConditions import views

from mosega_backend.ConfigHandler import *
configs = ConfigHandler.load_config('config.yaml')


API_PATH = configs['api']['backend']['Term']['view'] + '/' +configs['api']['title'] + '/' +\
           configs['api']['current_version'] + '/' + configs['api']['backend']['Term']['name'] + '/'

urlpatterns = [
    path(API_PATH, views.TermsAndConditionsList.as_view()),
    path(API_PATH + '<int:pk>/', views.TermsAndConditionsDetails.as_view()),
]