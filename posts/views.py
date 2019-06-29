from django.shortcuts import render
from .models import Posts

# Create your views here.
def main_page(request):
    # 모든 posts 출력
    posts = Posts.objects.all()

    return render(request, 'posts/main.html', {'posts': posts})


def create_post(request):
    pass