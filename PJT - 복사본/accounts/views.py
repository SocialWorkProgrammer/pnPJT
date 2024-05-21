from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
from rest_framework.response import Response
from rest_framework.decorators import api_view
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


@api_view(['GET'])
def product_histogram(request, username):
    if request.user.is_authenticated and request.user.username == username:
        # 사용자 정보 가져오기
        user = request.user
        
        # 사용자가 가입한 예금 및 적금 상품의 옵션 가져오기
        deposit_options = DepositOptions.objects.filter(deposit__contract_user=user)
        saving_options = SavingOptions.objects.filter(saving__contract_user=user)
        
        # 예금 상품과 적금 상품의 저축금리와 최고우대금리 데이터 가져오기
        deposit_products = deposit_options.values_list('deposit__fin_prdt_nm', flat=True)
        deposit_intr_rates = list(deposit_options.values_list('intr_rate', flat=True))
        deposit_intr_rates2 = list(deposit_options.values_list('intr_rate2', flat=True))
        
        saving_products = saving_options.values_list('saving__fin_prdt_nm', flat=True)
        saving_intr_rates = list(saving_options.values_list('intr_rate', flat=True))
        saving_intr_rates2 = list(saving_options.values_list('intr_rate2', flat=True))
        
        # 플롯 생성
        plt.figure(figsize=(12, 6))
        
        # 예금 상품의 히스토그램
        plt.bar(np.arange(len(deposit_intr_rates)), deposit_intr_rates, width=0.35, label='Deposit Interest Rate')
        plt.bar(np.arange(len(deposit_intr_rates))+0.35, deposit_intr_rates2, width=0.35, label='Deposit Max Preferential Rate')
        
        # 적금 상품의 히스토그램
        plt.bar(np.arange(len(saving_intr_rates)), saving_intr_rates, width=0.35, label='Saving Interest Rate')
        plt.bar(np.arange(len(saving_intr_rates))+0.35, saving_intr_rates2, width=0.35, label='Saving Max Preferential Rate')
        
        # x축 라벨 설정 예금 상품과 적금 상품의 상품명이 x축에 나타나도록 설정
        plt.xticks(np.arange(len(deposit_intr_rates)) + 0.35 / 2, list(deposit_products) + list(saving_products))
        
        # y축 라벨 설정
        plt.yticks(np.arange(0, 5, 0.5))
        
        # x축, y축 라벨 설정
        plt.xlabel('Product')
        plt.ylabel('Rate')
        
        # 제목 설정
        plt.title('Interest Rate Histogram')
        
        # 범례 설정
        plt.legend(loc='upper center')
        
        # 그리드 설정
        plt.grid(True)
        
        # 플롯 출력
        plt.show()
        
        return Response({"message": "Histogram generated successfully."}, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

