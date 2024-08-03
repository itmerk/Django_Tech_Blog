from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Test Page. Your blog index pages.")

def detial(request,post_id):
    return HttpResponse(f"Test Page. Your Detial page and DP testing. ID is {post_id}")

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("This is new url")