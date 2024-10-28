from django.urls import path
from . import views


urlpatterns =[
    path('',views.index,name='index'),
    path('specific',views.specific,name='specific'),
    path('getResponse',views.getResponse,name='getResponse'),
    path('chat_with_gpt',views.chat_with_gpt,name='chat_with_gpt'),
    ]
    
