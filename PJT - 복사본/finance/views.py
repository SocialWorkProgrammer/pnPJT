from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import requests
from django.http import HttpResponse
from django.conf import settings
from rest_framework.decorators import api_view
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, SavingProductsSerializer, SavingOptionsSerializer, DepositProductDetailSerializer, SavingProductDetailSerializer, DepositSignupSerializer, SavingSignupSerializer, SignupDepositSerializer, SignupSavingSerializer
from .models import DepositProducts, DepositOptions, SavingProducts, SavingOptions
from django.shortcuts import get_object_or_404, get_list_or_404
from accounts.models import User
# Create your views here.
@api_view(['GET'])
def data(request):
  PRODUCT_API_KEY=settings.PRODUCT_API_KEY
  Deposit_URL = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
  Saving_URL = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={PRODUCT_API_KEY}&topFinGrpNo=020000&pageNo=1'
  
  # 예금 상품 데이터 가져오기 및 baseList와 optionList 추출
  deposit_response = requests.get(Deposit_URL)
  if deposit_response.status_code != 200:
      return JsonResponse({'error': 'Failed to fetch deposit products', 'details': deposit_response.text}, status=deposit_response.status_code)

  deposit_data = deposit_response.json()
  deposit_base_list = deposit_data.get('result', {}).get('baseList', [])
  deposit_option_list = deposit_data.get('result', {}).get('optionList', [])


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
      'fin_prdt_nm' : item.get('fin_prdt_nm', -1),           # 예금 상품명
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
  saving_response = requests.get(Saving_URL)
  if saving_response.status_code != 200:
    return JsonResponse({'error': 'Failed to fetch saving products', 'details': saving_response.text}, status=saving_response.status_code)

  saving_data = saving_response.json()
  saving_base_list = saving_data.get('result', {}).get('baseList', [])
  saving_option_list = saving_data.get('result', {}).get('optionList', [])

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
      'fin_prdt_nm' : item.get('fin_prdt_nm', -1),           # 예금 상품명
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
      'rsrv_type_nm' : option.get('rsrv_type_nm', '-1'),             # 적립 유형명
      'intr_rate' : option.get('intr_rate', -1),                     # 이자율
      'intr_rate2' : option.get('intr_rate2', -1),                   # 최고 우대 금리
      'save_trm' : option.get('save_trm', -1),                       # 저축 기간 (개월)
    }
    
    # 적금 상품 옵션 시리얼라이저를 통해 데이터 검증 및 저장
    serializer = SavingOptionsSerializer(data = saving_option)
    if serializer.is_valid(raise_exception=True):
      serializer.save(saving=product)                                # 외래키로 예금 상품 객체를 지정
  return HttpResponse("정상적 처리 완료")




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
  deposits = DepositProducts.objects.filter(options__save_trm=save_trm).order_by('options__intr_rate')
  serializer = DepositProductDetailSerializer(deposits, many=True)
  return Response(serializer.data)

# 저축 기간별 예금 이자율 내림차순 정렬
@api_view(['GET'])
def deposit_descend_order(request, save_trm):
  deposits = DepositProducts.objects.filter(options__save_trm=save_trm).order_by('-options__intr_rate')
  serializer = DepositProductDetailSerializer(deposits, many=True)
  return Response(serializer.data)


# 저축 기간별 적금 이자율 오름차순 정렬
@api_view(['GET'])
def saving_ascend_order(request, save_trm):
  savings = SavingProducts.objects.filter(options__save_trm=save_trm).order_by('options__intr_rate')
  serializer = SavingProductDetailSerializer(savings, many=True)
  return Response(serializer.data)

# 저축 기간별 적금 이자율 내림차순 정렬
@api_view(['GET'])
def saving_descend_order(request, save_trm):
  savings = SavingProducts.objects.filter(options__save_trm=save_trm).order_by('-options__intr_rate')
  serializer = SavingProductDetailSerializer(savings, many=True)
  return Response(serializer.data)



# 특정 은행 예금 상품 가져오기
@api_view(['GET'])
def bank_deposit_products(request, fin_co_no):
  if DepositProducts.objects.filter(fin_co_no=fin_co_no).exists():
    deposits = DepositProducts.objects.filter(fin_co_no=fin_co_no)
    serializer = DepositProductsSerializer(deposits, many=True)
    return Response(serializer.data)
  

# 특정 은행 적금 상품 가져오기
@api_view(['GET'])
def bank_saving_products(request, fin_co_no):
  if SavingProducts.objects.filter(fin_co_no=fin_co_no).exists():
    savings = SavingProducts.objects.filter(fin_co_no=fin_co_no)
    serializer = SavingProductsSerializer(savings, many=True)
    return Response(serializer.data)
  
# 예금 상품 가입, 해지
@api_view(['GET', 'POST', 'DELETE'])
def signup_deposit(request, deposit_code):
  # 사용자 인증 여부 확인
  if not request.user.is_authenticated:
    return Response({"detail" : "로그인 하십시오"}, status=status.HTTP_401_UNAUTHORIZED)

  # 주어진 deposit_code에 해당하는 예금상품 가져오기
  deposit_product = get_object_or_404(DepositProducts, deposit_code=deposit_code)

  # GET일 때 예금상품 객체 직렬화하여 반환
  if request.method == 'GET':
    serializer = SignupDepositSerializer(deposit_product)
    return Response(serializer.data)
  
  # POST일 때 사용자가 예금상품 객체에 포함되지 않은 경우 추가
  elif request.method == 'POST':
    # 사용자가 contract_user에 포함되지 않은 경우
    if request.user not in deposit_product.contract_user.all():
      deposit_product.contract_user.add(request.user)   # 사용자 추가
      # 예금 상품 객체를 요청 데이터와 함께 부분적으로 직렬화
      serializer = SignupDepositSerializer(deposit_product, data=request.data, partial=True)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'detail':'상품 추가'}, status=status.HTTP_200_OK)
    else:
      # 사용자가 이미 포함되어 있는 경우
      return Response({'detail':'이미 가입했다'}, staus=status.HTTP_400_BAD_REQUEST)
    
  # DELETE일 때 사용자가 예금상품 객체에 포함되어 있는 경우 삭제
  elif request.method == 'DELETE':
    if request.user in deposit_product.contract_user.all():
      deposit_product.contract_user.remove(request.user)    # 사용자 제거
      return Response({"detail" : "삭제 완료"}, status=status.HTTP_204_NO_CONTENT)
    else:
      # 사용자가 포함되어 있지 않은 경우
      return Response({"detail":"가입한 상품이 아닙니다"}, status=status.HTTP_404_NOT_FOUND)
    
# 적금 상품 가입, 해지
@api_view(['GET', 'POST', 'DELETE'])
def signup_saving(request, saving_code):
  # 사용자 인증 여부 확인
  if not request.user.is_authenticated:
    return Response({"detail" : "로그인 하십시오"}, status=status.HTTP_401_UNAUTHORIZED)

  # 주어진 saving_code에 해당하는 적금상품 가져오기
  saving_product = get_object_or_404(SavingProducts, saving_code=saving_code)

  # GET일 때 적금상품 객체 직렬화하여 반환
  if request.method == 'GET':
    serializer = SignupSavingSerializer(saving_product)
    return Response(serializer.data)
  
  # POST일 때 사용자가 적금상품 객체에 포함되지 않은 경우 추가
  elif request.method == 'POST':
    # 사용자가 contract_user에 포함되지 않은 경우
    if request.user not in saving_product.contract_user.all():
      saving_product.contract_user.add(request.user)   # 사용자 추가
      # 적금 상품 객체를 요청 데이터와 함께 부분적으로 직렬화
      serializer = SignupSavingSerializer(saving_product, data=request.data, partial=True)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({'detail':'상품 추가'}, status=status.HTTP_200_OK)
    else:
      # 사용자가 이미 포함되어 있는 경우
      return Response({'detail':'이미 가입했다'}, staus=status.HTTP_400_BAD_REQUEST)
    
  # DELETE일 때 사용자가 예금상품 객체에 포함되어 있는 경우 삭제
  elif request.method == 'DELETE':
    if request.user in saving_product.contract_user.all():
      saving_product.contract_user.remove(request.user)    # 사용자 제거
      return Response({"detail" : "삭제 완료"}, status=status.HTTP_204_NO_CONTENT)
    else:
      # 사용자가 포함되어 있지 않은 경우
      return Response({"detail":"가입한 상품이 아닙니다"}, status=status.HTTP_404_NOT_FOUND)




# 사용자가 설정한 희망 예치 기간에 맞는 예금 및 적금 상품 추천
@api_view(['GET'])
def product_recommend_period(request):
  # 사용자 인증 확인
  if not request.user.is_authenticated:
    return Response({"detail":"로그인 해야 합니다"}, status=status.HTTP_401_UNAUTHORIZED)
  
  # 요청한 사용자 가져오기
  user = get_object_or_404(User, username=request.user.username)

  # 사용자의 희망 예금기간 가져오기
  desire_deposit_period = user.deposit_period

  # 희망 예치기간이 없는 경우 
  if not desire_deposit_period:
    return Response({"message": "희망기간을 입력해주십시오"}, status=status.HTTP_400_BAD_REQUEST)

  # 사용자가 원하는 상한 기간 계산(희망 예치 기간 + 2개월)
  max_period = desire_deposit_period + 2

  # 희망 조건에 맞는 예금 상품 필터링
  deposit_product = DepositProducts.objects.filter(depositoption__save_trm__lte=max_period)

  # 중복 제거 및 상위 10개 상품 선택
  deposit_product = list(set(deposit_product.order_by("-depositoption__intr_rate")[:10]))

  # 사용자의 희망 적금 기간 가져오기
  desire_saving_period = user.saving_period

  # 희망 적금기간이 없는 경우
  if not desire_saving_period:
    return Response({"message": "희망기간을 입력해주십시오"}, status=status.HTTP_400_BAD_REQUEST)
  
  # 사용자가 원하는 상한 기간 계산(희망 예치 기간 + 2개월)
  max_saving_period = desire_saving_period + 2

  # 희망 조건에 맞는 적금 상품 필터링
  saving_product = SavingProducts.objects.filter(savingoption__save_trm_lte=max_saving_period)

  # 중복 제거 및 상위 10개 상품 선택
  saving_product = list(set(saving_product.order_by("-savingoption__intr_rate")[:10]))

  # 필터링 된 예금 및 적금 상품 직렬화
  depositserializers = DepositProductDetailSerializer(deposit_product, many=True)
  savingserializers = SavingProductDetailSerializer(saving_product, many=True)

  # 응답 데이터 생성
  product_list = {
    "deposit_product":depositserializers.data,
    "saving_product":savingserializers.data
  }

  return Response(product_list)