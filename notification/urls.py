from django.urls import path
#from . import views
from notification.views import *

urlpatterns = [
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('send/', NotificationListCreateAPIView.as_view(), name='send_email'),
]
