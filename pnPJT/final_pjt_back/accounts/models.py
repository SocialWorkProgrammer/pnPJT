from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from finance.models import DepositProducts, SavingProducts

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)             # 유저 아이디
    name = models.CharField(max_length=30)                             # 유저 이름
    email = models.EmailField(max_length=254, blank=True, null=True)    # 유저 이메일
    age = models.IntegerField(blank=True, null=True)                    # 유저 나이
    money = models.IntegerField(blank=True, null=True)                  # 유저 예산
    salary = models.IntegerField(blank=True, null=True)                 # 유저 월급
    deposit_period = models.IntegerField(blank=True, null=True)         # 희망 예금 가입 기간
    saving_period = models.IntegerField(blank=True, null=True)         # 희망 적금 가입 기간
    # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함      
    financial_products = models.TextField(blank=True, null=True)        # 유저 가입 상품 목록 리스트
    sign_up_deposits = models.ManyToManyField(DepositProducts, related_name='users', blank=True)
    sign_up_savings = models.ManyToManyField(SavingProducts, related_name='users', blank=True)
    # superuser fields
    is_active = models.BooleanField(default=True)                       # 활동 여부
    is_staff = models.BooleanField(default=False)                       # 부매니저? 여부
    is_superuser = models.BooleanField(default=False)                   # 관리자 여부

    # 로그인 시 username 입력해야 함을 의미
    USERNAME_FIELD = 'username'

class CustomAccountAdapter(DefaultAccountAdapter):              
    # 회원가입 과정에서 사용자 모델의 추가 필드들을 처리하고, 사용자 생성 로직 커스터마이즈 하기 위해
    # 기본 DefaultAccountAdapter는 기본적인 사용자 생성 및 저장 기능만 제공
    # 커스터마이징을 통해 기본 사용자 모델에 없는 추가 필드들을 처리 가능
    def save_user(self, request, user, form, commit = True):
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        name = data.get("name")
        email = data.get("email")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        deposit_period = data.get("deposit_period")
        saving_period = data.get("saving_period")
        financial_product = data.get("financial_products")
        sign_up_deposits = data.get("sign_up_deposits")
        sign_up_savings = data.get("sign_up_savings")
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if name:
            user_field(user, "name", name)
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        if deposit_period:
            user.deposit_period = deposit_period
        if saving_period:
            user.saving_period = saving_period
        if financial_product:
            financial_products = user.financial_products.split(',')     # 기존 financial_products 필드를 리스트로 만들기
            financial_products.append(financial_product)        # 새로운 financial_product 값을 리스트에 추가
            if len(financial_products) > 1:
                financial_products = ','.join(financial_products) # 리스트를 다시 문자열로
            user_field(user, "financial_products", financial_products)  # 업데이트 된 financial products 값을 사용자 객체에 설정
        if sign_up_deposits:
            for deposit_code in sign_up_deposits:
                deposit = DepositProducts.objects.get(pk=deposit_code)
                user.sign_up_deposits.add(deposit)
        if sign_up_savings:
            for saving_code in sign_up_savings:
                saving = SavingProducts.objects.get(pk=saving_code)
                user.sign_up_savings.add(saving) 
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
        # Ability not to commit makes it easier to derive from
        # this adapter by adding
            user.save()
        return user
