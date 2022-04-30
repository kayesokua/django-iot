from django.urls import path
from .views import *
from camera.api.viewsets import *

urlpatterns = [
    path('/', camera_live, name='camera_live'),
    path('/capture', capture, name='capture'),
    path('/capture/<int:pk>', capture_detail, name='capture_detail'),
    path('/api/<int:pk>', PiImageDetailAV.as_view, name='PiImageDetail')
    
]