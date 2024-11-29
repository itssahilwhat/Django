from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "Blog/index.html")


def posts(request):
    return HttpResponse('<h1>Blog Posts</h1>')


def post(request, post_id):
    return HttpResponse(f'<h1>Blog Post {post_id}</h1>')