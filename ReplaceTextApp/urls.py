from django.urls import path
from ReplaceTextApp import views

# app_name = 'ReplaceTextApp'

urlpatterns = [
    path('<str:s>', views.index)
]