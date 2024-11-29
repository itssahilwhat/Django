from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "Blog/index.html")


def posts(request):
    pass


def post(request, post_id):
    pass