from django.urls import path, include
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.main_page, name="main"),
    path('post/', views.post, name="post"),
    path('post/<int:post_id>', views.post_deatil, name="post_detail"),
]
