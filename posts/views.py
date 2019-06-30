from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsModelForm

# Create your views here.
def main_page(request):
    # 모든 posts 출력
    posts = Posts.objects.all()

    return render(request, 'posts/main.html', {'posts': posts})


def create_post(request):
    if request.method == "POST":
        forms = PostsModelForm(request.POST)

        if forms.is_valid():
            created_post = forms.save(commit=False)
            created_post.writer = request.user
            created_post.save()
            
            return redirect('posts:main')
    else:
        # modelform 제공
        forms = PostsModelForm()
        
        return render(request, 'posts/post.html', {'forms': forms})