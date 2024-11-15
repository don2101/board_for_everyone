from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from accounts import account_check
from .models import Posts
from .forms import PostsModelForm
from .serializers import PostsSerializer


# Create your views here.
class PostView(APIView):
    def get(self, request, format=None):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        if account_check.is_authenticated(request.data["token"]):
            token = account_check.jwt_decode(request.data["token"])
            serializer = PostsSerializer(data=request.data, partial=True)
            
            if serializer.is_valid():
                writer = account_check.get_user(token['id'])
                serializer.save(writer=writer)
                
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class PostDetailView(APIView):
    def get(self, request, post_id, format=None):
        post = get_object_or_404(Posts, id=post_id)
        serializer = PostsSerializer(post)

        return Response(serializer.data)

    def put(self, request, post_id, format=None):
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

    def delete(self, request, post_id, format=None):
        post = Posts.objects.get(pk=post_id)

        if request.user == post.writer:
            post.delete()

            return Response(status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)
