from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('data/', views.data ),    # 상품 데이터 불러오기
    path('deposit/', views.deposit_products),    # 예금 상품 리스트
    path('deposit/<str:deposit_code>/', views.deposit_product_detail),      # 예금 상품 상세 정보
    path('saving/', views.saving_products),       # 적금 상품 리스트
    path('saving/<str:saving_code>/', views.saving_product_detail),        # 적금 상품 상세 정보
    path('deposit/ascend_order/6/', views.deposit_ascend_order, {'save_trm': '6'}),   # 저축 기간 6개월 예금 이자율 오름차순 정렬
    path('deposit/ascend_order/12/', views.deposit_ascend_order, {'save_trm': '12'}),   # 저축 기간 12개월 예금 이자율 오름차순 정렬
    path('deposit/ascend_order/24/', views.deposit_ascend_order, {'save_trm': '24'}),   # 저축 기간 24개월 예금 이자율 오름차순 정렬
    path('deposit/ascend_order/36/', views.deposit_ascend_order, {'save_trm': '36'}),   # 저축 기간 36개월 예금 이자율 오름차순 정렬
    path('deposit/descend_order/6/', views.deposit_descend_order, {'save_trm': '6'}),   # 저축 기간 6개월 예금 이자율 내림차순
    path('deposit/descend_order/12/', views.deposit_descend_order, {'save_trm': '12'}),   # 저축 기간 12개월 예금 이자율 내림차순
    path('deposit/descend_order/24/', views.deposit_descend_order, {'save_trm': '24'}),   # 저축 기간 24개월 예금 이자율 내림차순
    path('deposit/descend_order/36/', views.deposit_descend_order, {'save_trm': '36'}),   # 저축 기간 36개월 예금 이자율 내림차순
    path('saving/ascend_order/6/', views.saving_ascend_order, {'save_trm': '6'}),     # 저축 기간 6개월 적금 이자율 오름차순
    path('saving/ascend_order/12/', views.saving_ascend_order, {'save_trm': '12'}),   # 저축 기간 12개월 적금 이자율 오름차순
    path('saving/ascend_order/24/', views.saving_ascend_order, {'save_trm': '24'}),   # 저축 기간 24개월 적금 이자율 오름차순
    path('saving/ascend_order/36/', views.saving_ascend_order, {'save_trm': '36'}),   # 저축 기간 36개월 적금 이자율 오름차순
    path('saving/descend_order/6/', views.saving_descend_order, {'save_trm': '6'}),   # 저축 기간 6개월 예금 이자율 내림차순
    path('saving/descend_order/12/', views.saving_descend_order, {'save_trm': '12'}),   # 저축 기간 12개월 예금 이자율 내림차순
    path('saving/descend_order/24/', views.saving_descend_order, {'save_trm': '24'}),   # 저축 기간 24개월 예금 이자율 내림차순
    path('saving/descend_order/36/', views.saving_descend_order, {'save_trm': '36'}),   # 저축 기간 36개월 예금 이자율 내림차순
    path('deposit/<str:kor_co_nm>/', views.bank_deposit_products),    # 은행별 예금상품 필터링
    path('saving/<str:kor_co_nm>/', views.bank_saving_products),    # 은행별 적금상품 필터링



]