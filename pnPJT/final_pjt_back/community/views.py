from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

# Create your views here.

# 전체 게시판 목록(GET), 새 게시글 작성(POST)
@api_view(['GET', 'POST'])
def article_list(request):
  if request.method == 'GET':
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many = True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    if request.user.is_authenticated:
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
  
# 상세 게시글(GET), 삭제(DELETE), 수정(PUT)
@api_view(['GET', 'DELETE', 'PUT'])
def article(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  if request.method == 'GET':
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
  
  elif request.method == 'DELETE':
    if request.user.is_authenticated:
      if request.user == article.user:
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    else:
      return Response({ 'detail' : '권한 없음'}, status=status.HTTP_401_UNAUTHORIZED)
  
  elif request.method == 'PUT':
    if request.user.is_authenticated:
      if request.user == article.user:
        serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
      else:
        return Response({ 'detail' :  '권한 없음'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
      return Response({ 'detail' : '로그인 필요'}, status=status.HTTP_401_UNAUTHORIZED)
    

# 특정 게시물에 대한 댓글 작성
@api_view(['POST'])
def comment(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  if request.method == 'POST':
    if request.user.is_authenticated:
      serializer = CommentSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response({ 'detail' : '로그인 필요'}, status=status.HTTP_401_UNAUTHORIZED)


# 댓글 삭제 및 수정
@api_view(['DELETE', 'PUT'])
def comment_detail(request, article_pk, comment_pk):
  comment = get_object_or_404(Comment, pk=comment_pk)
  serializer = CommentSerializer(comment)
  if request.method == 'DELETE':
    if request.user.is_authenticated:
      if request.user == comment.user:
        comment.delete()
        return Response(serializer.data, status = status.HTTP_204_NO_CONTENT)
      else:
        return Response({ 'detail' :  '권한 없음'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
      return Response({ 'detail' : '로그인 필요'}, status=status.HTTP_401_UNAUTHORIZED)
  
  elif request.method == 'PUT':
    if request.user.is_authenticated:
      if request.user == comment.user:
        serializer = CommentSerializer(instance=comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
      else:
        return Response({ 'detail' :  '권한 없음'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
      return Response({ 'detail' : '로그인 필요'}, status=status.HTTP_401_UNAUTHORIZED) 

