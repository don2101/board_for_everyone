from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreationModelForm, UserLoginForm
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
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


def sign_in(request):
    if request.method == "POST":
        # login 시키고 main페이지로
        forms = UserLoginForm(request, request.POST)

        if forms.is_valid():
            login_user = forms.get_user()
            login(request, login_user)
            
            messages.success(request, "로그인 됐습니다")
            
            return redirect('posts:main')

    else:
        # login form 제공
        forms = UserLoginForm(request)

        return render(request, 'accounts/sign_in.html', {'forms': forms})


def sign_out(request):
    logout(request)
    messages.info(request, "로그아웃 됐습니다")

    return redirect('posts:main')


def mypage(request, user_name):
    # user가 작성한 모든 post 출력
    posts = request.user.posts_set.all()
    
    return render(request, 'accounts/mypage.html', {'posts': posts})
    