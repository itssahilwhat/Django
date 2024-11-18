from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def index(request):
    return HttpResponse('This works!')


def january(request):
    return HttpResponse('Eat no meat for the entire month')


def february(request):
    return HttpResponse('Walk for at least 20 minutes every day')


def march(request):
    return HttpResponse('Learn Django for at least 20 minutes every day')


def april(request):
    return HttpResponse('')


def may(request):
    return HttpResponse('May challenge')


def june(request):
    return HttpResponse('June challenge')


def july(request):
    return HttpResponse('July challenge')


def august(request):
    return HttpResponse('August challenge')


def september(request):
    return HttpResponse('September challenge')


def october(request):
    return HttpResponse('October challenge')


def november(request):
    return HttpResponse('November challenge')


def december(request):
    return HttpResponse('December challenge')


def monthly_challenge_by_number(request, month):
    months = list(range(1, 13))
    if month > len(months):
        return HttpResponse('Invalid month')
    return HttpResponse(months[month - 1])