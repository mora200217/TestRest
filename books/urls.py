from django.contrib import admin
from django.urls import path
from .views import GetInfo

urlpatterns = [
    path('traer/<int:pk>', GetInfo.as_view())
]