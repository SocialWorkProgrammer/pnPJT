from django.urls import path
from . import views

app_name='community'
urlpatterns = [
  path('', views.article_list),
  path('article/<int:article_pk>/', views.article_detail),
  path('article/<int:article_pk>/comment/create/', views.comment_create),
]