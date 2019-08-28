from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreationModelForm, UserLoginForm
from .serializers import UserSerializer, CustomJWTSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

import jwt

from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.conf import settings

# Create your views here.

User = get_user_model()

# 회원가입 기능
@api_view(['POST'])
def create_user(request):
    # 회원가입
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        
        try:
            user = authenticate(username=username, password=password)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        print(user)

        if user:

            payload = {
                'id': user.id,
                'email': user.email
            }

            jwt_token = { 'token': jwt.encode(payload, "SECRET_KEY") }
            print(jwt_token)
            return Response(jwt_token, status=status.HTTP_200_OK)
            


@api_view(['POST'])
def sign_in(request):
    serializer = CustomJWTSerializer(request.data)

    if serializer.is_valid():
        serializer.save()
    

def sign_out(request):
    logout(request)

    return redirect('posts:main')


def mypage(request, user_name):
    # user가 작성한 모든 post 출력
    posts = request.user.posts_set.all()
    
    return render(request, 'accounts/mypage.html', {'posts': posts})
    