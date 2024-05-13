from rest_framework import serializers
from .models import todo


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ('title', 'content')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = '__all__'