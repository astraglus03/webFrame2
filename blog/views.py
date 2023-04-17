from django.shortcuts import render
from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')  # -사용시 내림차순, 없을시 오름차순 pk는 primary key의 약자를 의미함

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # objects.get은 괄호안에 만족하는 레코드를 가져오라는 의미이다.

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post,
        }
    )
