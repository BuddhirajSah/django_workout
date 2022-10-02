from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def challenges(request):
    return HttpResponse("These are the challenges Bro - BuddyRaz!!")

