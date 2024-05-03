from django.urls import path
from . import views

app_name = 'algo'
urlpatterns = [
    path('', views.convert_csv_to_dataframe),
    path('b/', views.convert_blank_to_null),
    path('c/', views.convert_and_find_similar_age),

]