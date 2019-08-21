from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name = "accounts"

urlpatterns = [
    path('signup/', views.create_user, name="signup"),
    path('signin/', views.LoginView.as_view(), name="signin"),
    path('signout/', views.sign_out, name="signout"),
    path('token/', obtain_jwt_token, name="token_obtain"),
    path('token/verify/', verify_jwt_token, name="token_verity"),
    path('token/refresh/', refresh_jwt_token, name="token_refresh"),
    
    path('<str:user_name>/', views.mypage, name="mypage"),
]
