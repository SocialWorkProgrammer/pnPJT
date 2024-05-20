from django.urls import path
from . import views

app_name='profile'
urlpatterns = [
    path('<str:username>/', views.user_profile),
    path('<str:username>/detail/', views.user_detail),
    path('<str:username>/detail/histogram', views.product_histogram),
] 
