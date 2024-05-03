from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import numpy as np
import pandas as pd
import random
import json

array_length = 1000
random_range = 5000

# Create your views here.

# A. CSV 데이터를 DataFrame으로 변환 후 반환
# 1. numpy loadtxt 를 활용하는 방법
@api_view(['GET'])
def convert_csv_to_dataframe(request):
    arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
    columns = arr[0]
    arr = np.delete(arr, 0, 0)
    df = pd.DataFrame(arr, columns=columns)

    # records: 리스트 원소를 각각 하나의 레코드로 만들기 위해 주는 옵션
    data = df.to_dict('records')

    # JSON 형태로 응답합니다.
    return JsonResponse({ 'dat': data })


# 2. pandas 의 read_csv 를 이용하는 방법
# @api_view(['GET'])
# def convert_csv_to_dataframe(request):
#     # Read CSV file into a DataFrame
#     df = pd.read_csv('data/test_data.CSV', encoding='cp949')

#     # Convert DataFrame to a list of dictionaries
#     data = df.to_dict('records')

#     # Return response in JSON format
#     return JsonResponse({'dat': data}, json_dumps_params={'ensure_ascii': False})


# B. 결측치 처리 후 데이터 반환
@api_view(['GET'])
def convert_blank_to_null(request):
    arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
    columns = arr[0]
    arr = np.delete(arr, 0, 0)
    df = pd.DataFrame(arr, columns=columns)

    df.replace('','NULL', inplace=True)

    data = df.to_dict('records')

    return JsonResponse({ 'dat': data })



# C. 알고리즘 구현
df = None   # 전역 변수 df 선언
@api_view(['GET'])
def convert_and_find_similar_age(request):
    global df
    # CSV 데이터를 DataFrame으로 로드합니다.
    # 아직 DF가 로드되지 않은 경우 CSV 파일을 로드하여 DF로 변환
    if df is None:
        arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
        columns = arr[0]
        arr = np.delete(arr, 0, 0)
        df = pd.DataFrame(arr, columns=columns)
    
    # 나이 열을 숫자로 변환합니다.
    # pd.to_numeric 함수로 문자열을 숫자로 변환. errors='coerce'는 변환 불가 값이 있을 경우 NaN으로 처리
    df['나이'] = pd.to_numeric(df['나이'], errors='coerce')

    # 결측치를 제외한 데이터에 대해 평균을 계산합니다.
    # dropna() 함수를 사용하여 결측치를 제외하고 mean()함수를 사용해 평균 계산
    mean_age = df['나이'].dropna().mean()

    # 결측치가 아닌 행들로 이루어진 DataFrame을 생성합니다.
    # 결측치가 아닌 '나이' 열의 행들로 이루어진 새로운 DF 생성
    # 'dropna' 함수를 사용하여 '나이' 열에서 결측치가 있는 행들을 제외하고 
    # 'subset=['나이']'는 '나이' 열에 대해서만 결측치를 제외한다
    non_null_df = df.dropna(subset=['나이'])

    # 평균 나이에 가장 가까운 10개 행을 찾습니다.
    # 결측치가 아닌 행들로 이루어진 DataFrame에서 평균 나이에 가장 가까운 10개 행을 찾는다.
    # 'argsort()' 함수를 사용하여 평균과의 차이를 기준으로 행을 정렬하고, 가장 작은 차이를 가진 인덱스를 선택한다.
    # 이후 'iloc'을 사용하여 해당 인덱스에 해당하는 행을 선택한다.
    closest_rows = non_null_df.iloc[(non_null_df['나이'] - mean_age).abs().argsort()[:10]]

    # DataFrame을 사전의 리스트로 변환합니다.
    data = closest_rows.to_dict('records')

    # JSON 형식으로 응답합니다.
    return JsonResponse({'평균과 가장 가까운 나이 데이터': data})
