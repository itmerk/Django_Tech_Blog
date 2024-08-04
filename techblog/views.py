from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'techblog/index.html')

def detial(request,post_id):
    return render(request,'techblog/detial.html')

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("This is new url")