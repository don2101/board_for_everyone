from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.PostView.as_view(), name="main"),
    path('post/<int:post_id>/', views.PostDetailView.as_view(), name="post_detail"),
]
