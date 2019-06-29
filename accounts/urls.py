from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.create_user, name="signup"),
]
