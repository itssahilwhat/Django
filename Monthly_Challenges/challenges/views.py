from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "April challenge",
    "may": "May challenge",
    "june": "June challenge",
    "july": "July challenge",
    "august": "August challenge",
    "september": "September challenge",
    "october": "October challenge",
    "november": "November challenge",
    "december": "December challenge"
}


def index(request):
    return HttpResponse('This works!')


def january(request):
    return HttpResponse('Eat no meat for the entire month')


def february(request):
    return HttpResponse('Walk for at least 20 minutes every day')


def march(request):
    return HttpResponse('Learn Django for at least 20 minutes every day')


def april(request):
    return HttpResponse('April challenge')


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
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    return HttpResponse(f"Redirecting to {redirect_month} challenge")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')