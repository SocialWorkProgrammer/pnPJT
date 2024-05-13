from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import TodoListSerializer, TodoSerializer
from .models import todo
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def todo_list(request):
  if request.method == 'GET':
    todos = get_list_or_404(todo)
    serializer = TodoListSerializer(todos, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
