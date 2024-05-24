from django.http import JsonResponse
from rest_framework.response import Response
import requests
from django.conf import settings
from rest_framework.decorators import api_view
from .serializers import ExchangeSerializer
from .models import Exchange
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def exchange(request):
    EXCHANGE_API_KEY = settings.EXCHANGE_API_KEY
    Exchange_URL = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={EXCHANGE_API_KEY}&data=AP01'
    # API 호출해서 데이터 가져오기
    response = requests.get(Exchange_URL).json()
    # 기존 데이터 확인
    exist_response = Exchange.objects.all()

    if response:
        # 기존 데이터 존재 시 삭제 후 새로운 데이터 저장
        if exist_response:
            exist_response.delete()
        
        # 새로운 데이터 저장
        serializer = ExchangeSerializer(data=response, many = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # 새로운 데이터가 없으면 기존 데이터 그대로 반환
    else:
        if exist_response:
            serializer = ExchangeSerializer(exist_response, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({ 'message' : 'No data'}, status.HTTP_204_NO_CONTENT)   # 그냥 데이터가 아예 없는 경우
        