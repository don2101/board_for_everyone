from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from django.conf import settings

# Create your views here.

# 회원가입 기능
def create_user(request):
    if request.method == "POST":
        # 회원가입
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        # 회원가입 form 제공
        form = UserCreationForm()

        return render(request, 'accounts/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == "POST":
        # login 시키고 main페이지로
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login_user = form.get_user()
            login(request, login_user)

            return redirect('posts:main')

    else:
        # login form 제공
        form = AuthenticationForm(request)
        
        return render(request, 'accounts/sign_in.html', {'form': form})


def sign_out(request):
    logout(request)

    return redirect('posts:main')


def mypage(request, user_name):
    # user가 작성한 모든 post 출력
    posts = request.user.posts_set.all()
    
    return render(request, 'accounts/mypage.html', {'posts': posts})
    
