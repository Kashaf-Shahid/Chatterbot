from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
from dotenv import load_dotenv
import openai
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

load_dotenv()  

# Create your views here.
openai.api_key = os.getenv("OPENAI_API_KEY")

def index(request):
    return render(request, 'blog/index.html')

def getResponse(request):
    return HttpResponse("This is the getResponse view.")


def specific(request):

    list1=[1,2,3,4]
    return JsonResponse(list1,safe=False)



## GPT response
@csrf_exempt
def chatbot_response(request):
    if request.method == "GET":
        prompt = request.GET.get('prompt', '')
        if not prompt:
            return HttpResponse("No prompt provided.", status=400)

        try:
            # import pdb; pdb.set_trace() # for debugging
            
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert in Machine Learning."},
                    {"role": "user", "content": prompt}
                ]
            )

            bot_response = completion['choices'][0]['message']['content'].strip()
            print("bot_response", bot_response)

            return JsonResponse({'response': bot_response})

        except Exception as e:
            print("Exception occurred: ", e)
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)