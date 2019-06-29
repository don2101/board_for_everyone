from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.main_page, name="main"),
    path('post/', views.create_post, name="post"),
]
