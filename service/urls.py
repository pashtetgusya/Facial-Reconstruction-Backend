from django.urls import path
from service.views import ImageProcess, NetworkProcess

urlpatterns = [
    path('image_process', ImageProcess.as_view(), name='image_process'),
    path('network_process', NetworkProcess.as_view(), name='network_process'),
]
