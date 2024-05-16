from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
  nickname = serializers.CharField(
    required=False,
    allow_blank = True,
    max_length=255
  )
  
  def get_cleanded_data(self):
    return {
      'username': self.validated_data.get('username', ''),
      'password1': self.validated_data.get('password1', ''),
      'nickname': self.validated_data.get('nickname', ''),
    }