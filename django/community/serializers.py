from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = get_user_model()
    fields = ('username',)


# 전체 게시글
class ArticleListSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta : 
    model = Article
    fields = ('user', 'title', 'id', 'content')

# 댓글
class CommentSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  class Meta:
    model = Comment
    fields = ('user', 'content', 'updated_at', 'id')
    read_only_fields = ('article', 'user',)

# 상세 게시글(댓글 목록도 포함)
class ArticleSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)

  comments = CommentSerializer(many=True, read_only=True)
  class Meta:
    model = Article
    fields = '__all__'

  