from django.db import models

# Create your models here.

class Exchange(models.Model):
    cur_unit = models.CharField(max_length=30)     # 통화코드
    cur_nm = models.CharField(max_length=60)        # 국가/통화명
    ttb = models.CharField(max_length=40)          # 전신환(송금) 받을 때
    tts = models.CharField(max_length=40)          # 전신환(송금) 보낼 때
    deal_bas_r = models.CharField(max_length=20)   # 매매기준율
    bkpr = models.CharField(max_length=20)           # 장부가격
    yy_efee_r = models.CharField(max_length=20)      # 년환가료율
    ten_dd_efee_r = models.CharField(max_length=20)  # 10일 환가료율
    kftc_deal_bas_r = models.CharField(max_length=30) #서울외국환중개매매기준율
    kftc_bkpr = models.CharField(max_length=30)       #서울외국환중개장부가격