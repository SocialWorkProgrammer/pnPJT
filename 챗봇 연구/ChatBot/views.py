from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from openai import OpenAI
# from .models import Answer
# from .serializers import AnswerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['POST'])
def chat(request):
    if request.method == 'POST':
        prompt = request.POST.get('message')
        api_endpoint = 'https://api.openai.com/v1/chat/completions'
        api_key = 'sk-proj-lPC2bknyJ8zDeZS0Yrk7T3BlbkFJNpZKVZUMb5L4S1mySXgh'  # 본인의 OpenAI API 키로 대체
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': prompt}],
            'temperature': 0.8,
            'max_tokens': 1024,
            'top_p': 1,
            'frequency_penalty': 0.5,
            'presence_penalty': 0.5,
            'stop': ['Human']
        }
        
        response = requests.post(api_endpoint, headers=headers, json=data)
         # 응답 코드 확인
        if response.status_code != 200:
            return JsonResponse({'error': 'Failed to get response from OpenAI API'})
        
        try:
            ai_response = response.json()['choices'][0]['message']['content']
            return JsonResponse({'sender': '챗봇', 'content': ai_response})  # 수정된 부분: AI의 응답을 JSON 형식으로 클라이언트에게 반환
        except KeyError:
            return JsonResponse({'error': 'Invalid response from OpenAI API'})
        
        


#     client = OpenAI(
#         api_key='sk-proj-lPC2bknyJ8zDeZS0Yrk7T3BlbkFJNpZKVZUMb5L4S1mySXgh'
#     )
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "system",
#                 "content": "이제부터 너의 이름은 춘식이여"
#             },
#             {
#                 "role": "user",
#                 "content": request.data.get('question')
#             }
#         ],
#         model="gpt-3.5-turbo"
#     )
#     save_data = {
#         'answer': chat_completion.choices[0].message.content
#     }
#     serialzer = AnswerSerializer(data=save_data)
#     if serialzer.is_valid(raise_exception=True):
#         serialzer.save()
#     return Response(serialzer.data)