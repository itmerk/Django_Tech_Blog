from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse,include

# Create your views here.
def index(request):
    techblog_title = "Latest Tech updates"
    posts = [
        {'id':1,'title':'Post 1', 'content': 'Content of post 1'},
        {'id':2,'title':'Post 2', 'content': 'Content of post 2'},
        {'id':3,'title':'Post 3', 'content': 'Content of post 3'},
        {'id':4,'title':'Post 4', 'content': 'Content of post 4'},
        {'id':5,'title':'Post 5', 'content': 'Content of post 5'},
        {'id':6,'title':'Post 6', 'content': 'Content of post 6'}
    ]
    return render(request,'techblog/index.html',{"techblog_title":techblog_title, 'posts': posts})

def detial(request,post_id):
    return render(request,'techblog/detial.html')

def old_url_redirect(request):
    return redirect(reverse('techblog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is new url")