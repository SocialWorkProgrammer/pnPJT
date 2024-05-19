from django.contrib import admin
from django.urls import path
from . import views

app_name='community'
urlpatterns = [
    # 전체 게시판 목록(GET), 새 게시글 작성(POST)
    path('', views.article_list),    
    # 상세 게시글(GET), 삭제(DELETE) , 수정(PUT)
    path('article/<int:article_pk>/', views.article),  
    # 특정 게시물에 대한 댓글 작성
    path('article/<int:article_pk>/comment/', views.comment),
    # 특정 댓글 삭제, 수정
    path('article/<int:article_pk>/comment/<int:comment_pk>/', views.comment_detail)
]