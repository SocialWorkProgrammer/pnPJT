from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = ('contract_user',)

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('deposit',)

class DepositProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
    options = DepositOptionsSerializer(many=True, read_only = True)
    # many=True를 통해 여러 개의 DepositOptions 객체를 시리얼라이즈할 수 있도록 합니다.


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = ('contract_user',)

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('saving',)

class SavingProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'
    options = SavingOptionsSerializer(many=True, read_only = True)
    # many=True를 통해 여러 개의 DepositOptions 객체를 시리얼라이즈할 수 있도록 합니다.

class SignupDepositSerializer(serializers.ModelSerializer):
    depositoption_set = DepositOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = DepositProducts
        fields = ('deposit_code','fin_prdt_nm', 'kor_co_nm', 'depositoption_set')
    # Deposit 모델에서 'deposit_code', 'name', 'kor_co_nm' 필드와 함께
     # DepositOptionsSerializer로 시리얼라이즈된 'depositoption_set' 필드를 포함합니다.

class SignupSavingSerializer(serializers.ModelSerializer):
    savingoption_set = SavingOptionsSerializer(many=True, read_only=True)
    class Meta:
        model = SavingProducts
        fields = ('saving_code','fin_prdt_nm','kor_co_nm', 'savingoption_set')
    # Saving 모델에서 'saving_code', 'name', 'kor_co_nm' 필드와 함께
    # SavingOptionsSerializer로 시리얼라이즈된 'savingoption_set' 필드를 포함합니다.