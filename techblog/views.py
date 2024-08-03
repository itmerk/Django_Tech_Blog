from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Test Page. Your blog index pages.")

def detial(request):
    return HttpResponse("Test Page. Your Detial page.")