"""
URL configuration for finalpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 커뮤니티
    path('community/', include('community.urls')), 
    # 환율
    path('exchange/', include('exchange.urls')),  
    # 금융 상품 관련 모든 것  
    path('finance/', include('finance.urls')),    
    # 로그인 = /login, 로그아웃 =/logout(아마), 그 외 프로필 관련 url
    path('accounts/', include('dj_rest_auth.urls')),    
    # 회원가입
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    # 프로필
    path('profile/', include('accounts.urls')),
    # 챗봇
    path('chatbot/', include('chatbot.urls')), 
]
