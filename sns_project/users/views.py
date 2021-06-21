from django.shortcuts import render
from main.models import Post
from django.contrib.auth.models import User


def mypage(request):
    user = request.user
    posts = Post.objects.filter(writer=user)
    return render(request, 'users/mypage.html', {'posts':posts})

# Create your views here.
