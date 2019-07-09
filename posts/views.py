from django.shortcuts import render, redirect
from django.contrib.auth import models
from .models import Posts
from .forms import PostsModelForm

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PostsSerializer


# Create your views here.
@api_view(['GET'])
def main_page(request):
    # 모든 posts 출력
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_post(request):
    if request.method == "POST":
        serializer = PostsSerializer(data=request.data, partial=True)

        if request.user.is_authenticated:
            if serializer.is_valid():
                serializer.save(writer=request.user)
                
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    else:
        # modelform 제공

        return Response()
