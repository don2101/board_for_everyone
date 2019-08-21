from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreationModelForm, UserLoginForm
from .serializers import UserSerializer, CustomJWTSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework import status

from django.contrib.auth import login, logout
from django.contrib import messages

from django.conf import settings

# Create your views here.

# 회원가입 기능
@api_view(['POST'])
def create_user(request):
    # 회원가입
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class LoginView(ObtainJSONWebToken):
    serializer_class = CustomJWTSerializer

@api_view(['POST'])
def sign_in(request):
    serializer = CustomJWTSerializer(request.data)

    if serializer.is_valid():
        serializer.save()
    

def sign_out(request):
    logout(request)
    messages.info(request, "로그아웃 됐습니다")

    return redirect('posts:main')


def mypage(request, user_name):
    # user가 작성한 모든 post 출력
    posts = request.user.posts_set.all()
    
    return render(request, 'accounts/mypage.html', {'posts': posts})
    