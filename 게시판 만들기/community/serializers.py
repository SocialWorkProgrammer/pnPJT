from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

  class Meta:
    model = Article
    fields = ('title', )

class CommentSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Comment
    fields = ('content', )
    read_only_fields = ('article', )

class ArticleSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, read_only=True)
  class Meta:
    model = Article
    fields = ('title', 'content', 'comments', )
