from django.urls import path
from camera.views import *

urlpatterns = [
    path('/', setup, name='setup'),
    path('/capture', PiImageAV.as_view(), name='capture')
]