from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .serializers import UserSerializer

import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

import jwt
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model, authenticate
from django.conf import settings

# Create your views here.

User = get_user_model()

# 회원가입 기능
@api_view(['POST'])
def create_user(request):
    # 회원가입
    request.data['password'] = make_password(request.data.get('password'))
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']

    user = authenticate(request, username=username, password=password)

    if user:

        payload = {
            'id': user.id,
            'nickname': user.username,
            'email': user.email,
            'exp': datetime.datetime.now() + datetime.timedelta(seconds=100)
        }
        
        jwt_token = jwt.encode(payload, "secret", algorithm="HS256")
        
        return Response(jwt_token, status=status.HTTP_200_OK)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    try:
        token = request.data['token']
        result = jwt.decode(token, "secret", algorithms="HS256")
        
        return Response(status=status.HTTP_200_OK)
    except jwt.ExpiredSignatureError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
def mypage(request, user_name):
    # user가 작성한 모든 post 출력
    posts = request.user.posts_set.all()
    
    return render(request, 'accounts/mypage.html', {'posts': posts})
    