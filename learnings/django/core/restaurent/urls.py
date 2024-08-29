from django.contrib import admin
from django.urls import path
from restaurent.views import *

urlpatterns = [
    path('receipes/',receipes,name='receipes')   
]
