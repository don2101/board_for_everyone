from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Posts
from .forms import PostsModelForm
from .serializers import PostsSerializer


# Create your views here.
@api_view(['GET'])
def main_page(request):
    # 모든 posts 출력
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def post(request):
    if request.user.is_authenticated:
        serializer = PostsSerializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(writer=request.user)
            
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def post_deatil(request, post_id):
    if request.method == "GET":
        post = get_object_or_404(Posts, id=post_id)
        print(post.writer)
        serializer = PostsSerializer(post)

        return Response(serializer.data)

    elif request.method == "PUT":
        post = get_object_or_404(Posts, id=post_id)
        
        if request.user == post.writer:
            serializer = PostsSerializer(post, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save(writer=request.user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    else:
        post = Posts.objects.get(pk=post_id)

        if request.user == post.writer:
            post.delete()

            return Response(status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)


