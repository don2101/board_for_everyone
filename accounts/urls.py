from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.create_user, name="signup"),
    path('signin/', views.LoginView.as_view(), name="signin"),
    path('signout/', views.logout, name="signout"),
    
    path('<str:user_name>/', views.mypage, name="mypage"),
]
