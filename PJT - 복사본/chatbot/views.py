from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from openai import OpenAI
# from .models import Answer
# from .serializers import AnswerSerializer
# from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser



@csrf_exempt
@api_view(['POST'])
def chat(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            prompt = data.get('message')
            
            if not prompt:
                return JsonResponse({'error': 'Message cannot be null or empty'}, status=400)
            
            api_endpoint = 'https://api.openai.com/v1/chat/completions'
            api_key = 'sk-proj-lPC2bknyJ8zDeZS0Yrk7T3BlbkFJNpZKVZUMb5L4S1mySXgh'  # 본인의 OpenAI API 키로 대체
            
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            }
            
            payload = {
                'model': 'gpt-3.5-turbo',
                'messages': [{'role': 'user', 'content': prompt}],
                'temperature': 0.8,
                'max_tokens': 1024,
                'top_p': 1,
                'frequency_penalty': 0.5,
                'presence_penalty': 0.5,
                'stop': ['Human']
            }
            
            response = requests.post(api_endpoint, headers=headers, json=payload)
            
            if response.status_code != 200:
                print(f"OpenAI API error: {response.status_code}, {response.text}")
                return JsonResponse({'error': 'Failed to get response from OpenAI API'}, status=response.status_code)
            
            response_json = response.json()
            try:
                ai_response = response_json['choices'][0]['message']['content']
                response_message = f"{ai_response}"
                return HttpResponse(response_message, content_type='text/plain')
            except (KeyError, IndexError) as e:
                print(f"Error parsing response: {e}")
                print(response_json)  # 응답 내용 로그
                return JsonResponse({'error': 'Invalid response format from OpenAI API'}, status=500)
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

        
        


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
