from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()  

# Create your views here.

openai.api_key =os.getenv("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")


def index(request):
    return render(request, 'blog/index.html')

def getResponse(request):
    return HttpResponse("This is the getResponse view.")


def specific(request):

    list1=[1,2,3,4]
    return JsonResponse(list1,safe=False)

def chat_with_gpt(request):
    prompt = request.GET.get('prompt','' )  
    if not prompt:
        return HttpResponse("No prompt provided.", status=400)

    
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        chat_response = response.choices[0].message.content.strip()
        return HttpResponse(chat_response)
    
    
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)