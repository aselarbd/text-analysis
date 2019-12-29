from django.urls import path

from PrivacyPolicy import views

from Handlers.Config.ConfigHandler import *
configs = ConfigHandler.load_config('config.yaml')


API_PATH = configs['api']['backend']['Policy']['view'] + '/' +configs['api']['title'] + '/' +\
           configs['api']['current_version'] + '/' + configs['api']['backend']['Policy']['name'] + '/'

urlpatterns = [
    path(API_PATH, views.PrivacyPolicyList.as_view()),
    path(API_PATH + '<int:ID>/', views.PrivacyPolicyDetails.as_view()),
]
