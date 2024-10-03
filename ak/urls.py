from django.urls import path,include
from .views import *
urlpatterns = [
    path('employee/',trigger_signal,name='employee'),
    path('rectangle/',Rectangle.as_view(),name='rectangle')
]
