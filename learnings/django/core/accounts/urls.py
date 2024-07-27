from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path("home/", Hello,name='home'),
    path('crud/',CrudView.as_view(),name='crud')
]
