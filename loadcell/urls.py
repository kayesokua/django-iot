from django.urls import path
from loadcell.views import *

urlpatterns = [
    path('/', info, name='info'),
    path('/test', test, name='test')
]