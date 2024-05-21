from rest_framework import serializers
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from finance.serializers import SignupDepositSerializer, SignupSavingSerializer

# 필드 정의
class CustomRegisterSerializer(RegisterSerializer):
  username = serializers.CharField(max_length=30)       # 로그인 아이디, 입력 필수
  name = serializers.CharField(max_length=30)   # 사용자 실명, 입력 필수
  email = serializers.EmailField(required=False)      # 이메일, 마찬가지로 필수 아님


  # 유효성 검사 완료된 데이터 반환
  # validated_data 속성 사용하여 폼 데이터 가져오고 각 필드가 없을 경우 기본값 설정
  def get_cleaned_data(self):
    return {
      'username': self.validated_data.get('username', ''),
      'email': self.validated_data.get('email', ''),
      'password1': self.validated_data.get('password1', ''),
      'name': self.validated_data.get('name', ''),
    }
  

  # 새로운 사용자를 생성하고 사용자를 데이터베이스에 저장
  def save(self, request):
    adapter = get_adapter()                       # DefaultAccountAdapter 인스턴스 가져오는 것
    user = adapter.new_user(request)              # 새로운 사용자 인스턴스 생성
    self.cleaned_data = self.get_cleaned_data()   # 유효성 검사 통과 데이터 가져오기
    adapter.save_user(request, user, self)        # 사용자 데이터 저장
    self.custom_signup(request, user)             # 추가적인 사용자 정의 가입 로직 처리
    return user
  

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'name', 'email', 'age', 'money', 'salary',)
    read_only_fields = ('id', 'username', 'name', )


class UserDetailSerializer(serializers.ModelSerializer):
  sign_up_deposits= SignupDepositSerializer(many=True)
  sign_up_savings = SignupSavingSerializer(many=True)
  class Meta:
    model = User
    fields = '__all__'
    read_only_fields = ('id', 'username', 'name', )

