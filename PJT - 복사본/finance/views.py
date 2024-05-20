from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
import requests
from django.conf import settings
from rest_framework.decorators import api_view
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer, DepositProductDetailSerializer, SavingProductDetailSerializer, DepositSignupSerializer, SavingSignupSerializer, SignupDepositSerializer, SignupSavingSerializer
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.
@api_view(['GET'])
def data(request):
  PRODUCT_API_KEY=settings.PRODUCT_API_KEY
  Deposit_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
  Saving_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
  
  # 예금 상품 데이터 가져오기 및 baseList와 optionList 추출
  deposit_response = requests.get(Deposit_URL).json()
  deposit_base_list = deposit_response.get('result').get('baseList')
  deposit_option_list = deposit_response.get('result').get('optionList')

  # 예금 상품 목록 정보 저장
  for item in deposit_base_list:
    # 이미 존재하는 예금 상품인지 확인
    if DepositProducts.objects.filter(deposit_code=item.get('fin_prdt_cd')).exists():
      # 이미 존재하면 다음으로 넘어감
      continue
    # 새로운 예금 상품 데이터 구성
    deposit_product = {
      'deposit_code' : item.get('fin_prdt_cd', -1),   # 예금 상품 코드
      'fin_co_no' : item.get('fin_co_no', -1),        # 금융 회사 번호
      'kor_co_nm' : item.get('kor_co_nm', -1),        # 금융 회사명
      'name' : item.get('fin_prdt_nm', -1),           # 예금 상품명
      'join_way' : item.get('join_way', -1),          # 가입 방법
      'mtrt_int' : item.get('mtrt_int', -1),          # 만기 후 이자
      'spcl_cnd' : item.get('spcl_cnd', -1),          # 우대 조건
      'join_deny' : item.get('join_deny', -1),        # 가입 제한
      'join_member' : item.get('join_member', -1),    # 가입 대상
      'etc_note' : item.get('etc_note', -1),          # 기타 유의사항
      'max_limit' : item.get('max_limit', -1),        # 최고 한도   
    }
    # 예금 상품 시리얼라이저를 통해 데이터 검증 및 저장
    serializer = DepositProductsSerializer(data = deposit_product)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
  
  # 예금 상품 옵션 목록 정보 저장
  for option in deposit_option_list:
    prdt_cd = option.get('fin_prdt_cd', '-1')   # 예금 상품 코드
    product = DepositProducts.objects.get(deposit_code=prdt_cd)   # 해당 코드의 예금 상품 객체 가져오기
    # 새로운 예금 상품  
    deposit_option = {
      'intr_rate_type_nm' : option.get('intr_rate_type_nm', '-1'),   # 이자율 유형명
      'intr_rate' : option.get('intr_rate', -1),                     # 이자율
      'intr_rate2' : option.get('intr_rate2', -1),                   # 최고 우대 금리
      'save_trm' : option.get('save_trm', -1),                       # 저축 기간 (개월)
    }
    
    # 예금 상품 옵션 시리얼라이저를 통해 데이터 검증 및 저장
    serializer = DepositOptionsSerializer(data = deposit_option)
    if serializer.is_valid(raise_exception=True):
      serializer.save(deposit=product)                                # 외래키로 예금 상품 객체를 지정


# 적금 상품 데이터 가져오기 및 baseList와 optionList 추출
  saving_response = requests.get(Saving_URL).json()
  saving_base_list = saving_response.get('result').get('baseList')
  saving_option_list = saving_response.get('result').get('optionList')

  # 적금 상품 목록 정보 저장
  for item in saving_base_list:
    # 이미 존재하는 적금 상품인지 확인
    if SavingProducts.objects.filter(saving_code=item.get('fin_prdt_cd')).exists():
      # 이미 존재하면 다음으로 넘어감
      continue
    # 새로운 적금 상품 데이터 구성
    saving_product = {
      'saving_code' : item.get('fin_prdt_cd', -1),    # 적금 상품 코드
      'fin_co_no' : item.get('fin_co_no', -1),        # 금융 회사 번호
      'kor_co_nm' : item.get('kor_co_nm', -1),        # 금융 회사명
      'name' : item.get('fin_prdt_nm', -1),           # 예금 상품명
      'join_way' : item.get('join_way', -1),          # 가입 방법
      'mtrt_int' : item.get('mtrt_int', -1),          # 만기 후 이자
      'spcl_cnd' : item.get('spcl_cnd', -1),          # 우대 조건
      'join_deny' : item.get('join_deny', -1),        # 가입 제한
      'join_member' : item.get('join_member', -1),    # 가입 대상
      'etc_note' : item.get('etc_note', -1),          # 기타 유의사항
      'max_limit' : item.get('max_limit', -1),        # 최고 한도   
    }
    # 적금 상품 시리얼라이저를 통해 데이터 검증 및 저장
    serializer = SavingProductsSerializer(data = saving_product)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
  
  # 적금 상품 옵션 목록 정보 저장
  for option in saving_option_list:
    prdt_cd = option.get('fin_prdt_cd', '-1')   # 적금 상품 코드
    product = SavingProducts.objects.get(saving_code=prdt_cd)   # 해당 코드의 적금 상품 객체 가져오기
    # 새로운 적금 상품  
    saving_option = {
      'intr_rate_type_nm' : option.get('intr_rate_type_nm', '-1'),   # 이자율 유형명
      'intr_rate' : option.get('intr_rate', -1),                     # 이자율
      'intr_rate2' : option.get('intr_rate2', -1),                   # 최고 우대 금리
      'save_trm' : option.get('save_trm', -1),                       # 저축 기간 (개월)
    }
    
    # 적금 상품 옵션 시리얼라이저를 통해 데이터 검증 및 저장
    serializer = SavingOptionsSerializer(data = saving_option)
    if serializer.is_valid(raise_exception=True):
      serializer.save(saving=product)                                # 외래키로 예금 상품 객체를 지정



# 예금 상품 리스트 출력
@api_view(['GET'])
def deposit_products(request):
  deposit_products = DepositProducts.objects.all()
  serializers = DepositProductsSerializer(deposit_products, many=True)
  return Response(serializers.data)

# 예금 상품 상세 정보-예금 상품 코드 입력
@api_view(['GET'])
def deposit_product_detail(request, deposit_code):
  deposit_product = get_object_or_404(DepositProducts, deposit_code=deposit_code)
  serializer = DepositProductDetailSerializer(deposit_product)
  return Response(serializer.data)

# 적금 상품 리스트 출력
@api_view(['GET'])
def saving_products(request):
  saving_products = SavingProducts.objects.all()
  serializers = SavingProductsSerializer(saving_products, many=True)
  return Response(serializers.data)

# 적금 상품 상세 정보 - 적금 상품 코드 입력
@api_view(['GET'])
def saving_product_detail(request, saving_code):
  saving_product = get_object_or_404(SavingProducts, saving_code=saving_code)
  serializer = SavingProductDetailSerializer(saving_product)
  return Response(serializer.data)


# 저축 기간별 예금 이자율 오름차순 정렬
@api_view(['GET'])
def deposit_ascend_order(request, save_trm):
  deposits = DepositProducts.objects.filter(depositoption__save_trm=save_trm).order_by('depositoption__intr_rate')
  serializer = DepositProductDetailSerializer(deposits, many=True)
  return Response(serializer.data)

# 저축 기간별 예금 이자율 내림차순 정렬
@api_view(['GET'])
def deposit_descend_order(request, save_trm):
  deposits = DepositProducts.objects.filter(depositoption__save_trm=save_trm).order_by('-depositoption__intr_rate')
  serializer = DepositProductDetailSerializer(deposits, many=True)
  return Response(serializer.data)


# 저축 기간별 적금 이자율 오름차순 정렬
@api_view(['GET'])
def saving_ascend_order(request, save_trm):
  savings = SavingProducts.objects.filter(savingoption__save_trm=save_trm).order_by('savingoption__intr_rate')
  serializer = SavingProductDetailSerializer(savings, many=True)
  return Response(serializer.data)

# 저축 기간별 적금 이자율 내림차순 정렬
@api_view(['GET'])
def saving_descend_order(request, save_trm):
  savings = SavingProducts.objects.filter(savingoption__save_trm=save_trm).order_by('-savingoption__intr_rate')
  serializer = SavingProductDetailSerializer(savings, many=True)
  return Response(serializer.data)



# 특정 은행 예금 상품 가져오기
@api_view(['GET'])
def bank_deposit_products(request, kor_co_nm):
  if DepositProducts.objects.filter(kor_co_nm=kor_co_nm).exists():
    deposits = DepositProducts.objects.filter(kor_co_nm=kor_co_nm)
    serializer = DepositProductsSerializer(deposits, many=True)
    return Response(serializer.data)
  

# 특정 은행 적금 상품 가져오기
@api_view(['GET'])
def bank_saving_products(request, kor_co_nm):
  if SavingProducts.objects.filter(kor_co_nm=kor_co_nm).exists():
    savings = SavingProducts.objects.filter(kor_co_nm=kor_co_nm)
    serializer = SavingProductsSerializer(savings, many=True)
    return Response(serializer.data)
  







