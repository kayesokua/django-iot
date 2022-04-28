from django.urls import path
from loadcell.views import *

urlpatterns = [
    path('/', setup, name='setup'),
    path('/test', weigh_test, name='weigh_test')
]