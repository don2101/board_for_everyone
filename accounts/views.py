from django.shortcuts import render, redirect

# module for rest_framework
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# module for User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model, authenticate

# module for jwt
from simple_board import jwt_parser


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
        payload = jwt_parser.set_payload(user)
        jwt_token = jwt_parser.encode(payload)
        
        return Response(jwt_token, status=status.HTTP_200_OK)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout(request):
    token = request.data['token']
    result = jwt_parser.decode(token)
    
    if result: 
        return Response(status=status.HTTP_200_OK)
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
def mypage(request, user_name):
    # user가 작성한 모든 post 출력
    posts = request.user.posts_set.all()
    
    return render(request, 'accounts/mypage.html', {'posts': posts})
    