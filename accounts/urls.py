from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('create/', views.create_user),
]
