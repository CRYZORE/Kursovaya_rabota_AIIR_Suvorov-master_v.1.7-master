from django.urls import path
from summary import views

# app_name = 'summary'

urlpatterns = [
    path('<str:s>', views.index)
]