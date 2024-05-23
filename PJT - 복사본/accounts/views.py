from django.shortcuts import render
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc
# from io import BytesIO
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from finance.models import DepositProducts, SavingProducts, DepositOptions, SavingOptions

# Create your views here.
# 사용자 프로필 가져오기 - 유저 모델만
@api_view(['GET'])
def user_profile(request, username):
    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), username=username)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    else:
        return Response({"message":"로그인이 필요하다"}, status=status.HTTP_401_UNAUTHORIZED)


# 사용자 상세 정보 가져오기 - 유저 모델 + 가입 예적금 상품 & 
@api_view(['GET', 'PUT'])
def user_detail(request, username):
    # 사용자가 인증되어 있고, 요청된 사용자와 현재 사용자가 동일한 경우에만 실행
    if request.user.is_authenticated and request.user.username == username:
        # GET 요청 처리
        if request.method == 'GET':
            # 요청된 사용자를 가져오거나 404 에러 반환
            user = get_object_or_404(get_user_model(), username=username)
            # 사용자 정보를 시리얼라이즈하여 반환
            serializer = UserDetailSerializer(user)
            return Response(serializer.data)
        # PUT 요청 처리
        elif request.method == 'PUT':
            # 요청된 사용자를 가져오거나 404 에러 반환
            user = get_object_or_404(get_user_model(), username=username)
            # 전달된 데이터를 사용하여 시리얼라이저 생성
            serializer = UserDetailSerializer(instance=user, data=request.data, partial=True)
            # 시리얼라이저 유효성 검사 및 저장
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)  # 현재 사용자로 저장
                return Response(serializer.data, status=status.HTTP_200_OK)  # 성공적으로 업데이트된 데이터 반환
    # 사용자가 인증되지 않았거나 요청된 사용자와 현재 사용자가 다른 경우 400 Bad Request 반환
    return Response(status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def deposit_product_histogram(request, username):
#     if request.user.is_authenticated and request.user.username == username:
#         # 사용자 정보 가져오기
#         user = request.user
        
#         # 사용자가 가입한 예금 및 적금 상품 가져오기
#         deposit_products = user.sign_up_deposits.all()

#     product_names = []
#     base_rates = []
#     max_preferential_rates = []

#     for product in deposit_products:
#         product_names.append(product.fin_prdt_nm)
#         for option in product.options.all():
#             base_rates.append(option.intr_rate)
#             max_preferential_rates.append(option.intr_rate2)

#     # 한글 폰트 설정
#         font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # 이 경로는 시스템에 따라 다를 수 있습니다
#         font_name = font_manager.FontProperties(fname=font_path).get_name()
#         rc('font', family=font_name)

#     fig, ax = plt.subplots()
#     bar_width = 0.35
#     index = range(len(product_names))

#     bars1 = plt.bar(index, base_rates, bar_width, label='기초 금리')
#     bars2 = plt.bar([i + bar_width for i in index], max_preferential_rates, bar_width, label='최고 우대금리 금리')

#     plt.xlabel('상품명')
#     plt.ylabel('금리')
#     plt.title('가입한 상품 금리')
#     plt.xticks([i + bar_width / 2 for i in index], product_names, rotation=45)
#     plt.legend()

#     buf = BytesIO()
#     plt.savefig(buf, format='png')
#     plt.close(fig)
#     buf.seek(0)
#     return HttpResponse(buf, content_type='image/png')