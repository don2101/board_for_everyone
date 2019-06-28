from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# 회원가입 기능
def create_user(request):
    if request.method == "POST":
        # 회원가입
        pass
    else:
        # 회원가입 form 제공
        form = UserCreationForm()

        return render(request, 'accounts/sign_up.html', {'form': form})