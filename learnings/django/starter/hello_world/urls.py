from django.urls import path
from hello_world.views import *
urlpatterns = [
    path('hello/',helloWorld,name='hello')
]