# make_data.py 파일은 랜덤한 더미 데이터를 만드는 예시 파일입니다.
# 반드시, 사용하는 필드를 확인한 후 본인의 프로젝트에 맞게 수정하여 진행해야 합니다.

# [참고] 현재 코드는 아래 User 모델을 기준으로 작성되어 있습니다.
"""
class User(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    money = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    # 가입한 상품 목록 리스트를 ,로 구분된 문자열로 저장함
    financial_products = models.TextField(blank=True, null=True)

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
"""

from django.conf import settings
import random
import requests

first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지'
last_name_samples = '준윤우원호후서연아은진'

# 무작위 사용자 이름 생성
def random_name():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))


# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = '142dc84483391d09064354c8ee7e7f30'

# 금융상품 코드 저장 리스트
financial_products = []

# API 요청 파라미터
params = {
    'auth': API_KEY,
    # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
    'topFinGrpNo': '020000',
    'pageNo': 1,
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# JSON 파일 필드 키
dict_keys = [
    'username',
    'gender',
    'financial_products',
    'age',
    'money',
    'salary',
]

# json 파일 만들기
import json
from collections import OrderedDict

# 사용자 정보 담을 oRDEREDdICT 객체 생성
file = OrderedDict()

# 중복되지 않는 유저 이름 생성 리스트
name_list = []
N = 10000
i = 0

# 중복되지 않는 사용자 이름 생성
while i < N:
    rn = random_name()
    if rn in name_list:
        continue

    name_list.append(rn)
    i += 1


# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = 'accounts/fixtures/accounts/user_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:        # JSON 파일 생성하고 데이터 작성
    f.write('[')
    # 무작위 데이터 생성 후 JSON 파일에 작성
    for i in range(N):
        # 랜덤한 데이터를 삽입
        file['model'] = 'accounts.User'
        file['pk'] = i + 1
        file['fields'] = {
            'username' : 'tester'+str(i),   # 로그인 시 입력할 유저 아이디
            'name': name_list[i],  # 유저 이름 랜덤 생성
            # 랜덤한 0~5개의 상품을 가입하도록 삽입됨
            'financial_products': ','.join(
                [
                    random.choice(financial_products)
                    for _ in range(random.randint(0, 5))
                ]
            ),  # 금융 상품 리스트
            'age': random.randint(1, 100),  # 나이
            'money': random.randrange(0, 100000000, 100000),  # 현재 가진 금액
            'salary': random.randrange(0, 1500000000, 1000000),  # 연봉
            'password': '1234',
            'is_active': True,
            'is_staff': False,
            'is_superuser': False,
        }

        json.dump(file, f, ensure_ascii=False, indent='\t')
        if i != N - 1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
