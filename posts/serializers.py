from rest_framework import serializers
from .models import Posts


class PostsSerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField()

    class Meta:
        model = Posts
        fields = ['writer', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
