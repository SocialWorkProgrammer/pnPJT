from django.db import models
from django.conf import settings
# Create your models here.

class DepositProducts(models.Model):
    deposit_code = models.TextField()        # 금융 상품 코드
    fin_co_no = models.TextField()          # 금융 회사 코드
    kor_co_nm = models.TextField()          # 금융회사명
    fin_prdt_nm = models.TextField()        # 금융 상품명
    join_way = models.TextField()           # 가입 방법
    mtrt_int = models.TextField()           # 만기 후 이자율 설명
    spcl_cnd = models.TextField()           # 우대 조건
    join_deny = models.IntegerField()       # 가입 제한 (1: 제한 없음 / 2: 서민 전용 / 3: 일부 제한)
    join_member = models.TextField()        # 가입 대상
    etc_note = models.TextField()           # 기타 유의사항
    max_limit = models.IntegerField(null=True, blank=True)       # 최고한도
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='sign_up_deposits')   # 가입자



class DepositOptions(models.Model):
    deposit = models.ForeignKey(DepositProducts, related_name='options', on_delete = models.CASCADE)    # 외래키
    intr_rate_type_nm = models.CharField(max_length=100)                        # 저축금리 유형명
    intr_rate = models.FloatField()                                             # 저축금리
    intr_rate2 = models.FloatField()                                            # 최고우대금리
    save_trm = models.IntegerField()                                            # 저축기간(단위:개월)


class SavingProducts(models.Model):
    saving_code = models.TextField()        # 금융 상품 코드
    fin_co_no = models.TextField()          # 금융 회사 코드
    kor_co_nm = models.TextField()          # 금융회사명
    fin_prdt_nm = models.TextField()        # 금융 상품명
    join_way = models.TextField()           # 가입 방법
    mtrt_int = models.TextField()           # 만기 후 이자율 설명
    join_deny = models.IntegerField()       # 가입 제한 (1: 제한 없음 / 2: 서민 전용 / 3: 일부 제한)
    join_member = models.TextField()        # 가입 대상
    etc_note = models.TextField()           # 기타 유의사항
    max_limit = models.IntegerField(null=True, blank=True)      # 최고한도
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='sign_up_savings')    # 가입자

class SavingOptions(models.Model):
    saving = models.ForeignKey(SavingProducts, related_name='options', on_delete = models.CASCADE)     # 외래키
    intr_rate_type_nm = models.CharField(max_length=100)                        # 저축 금리 유형명
    rsrv_type_nm = models.CharField(max_length=100)                             # 적립 유형명
    save_trm = models.IntegerField()                                            # 저축 기간(개월)
    intr_rate = models.FloatField()                                             # 저축금리
    intr_rate2 = models.FloatField()                                            # 최고우대금리