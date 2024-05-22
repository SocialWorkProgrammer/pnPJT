from django.urls import path
from . import views

app_name='ChatBot'
urlpatterns = [
    path('chat/', views.chat),
]
