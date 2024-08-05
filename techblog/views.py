from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post,Aboutus
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.
#posts = [
        #{'id':1,'title':'Post 1', 'content': 'Content of post 1'},
        #{'id':2,'title':'Post 2', 'content': 'Content of post 2'},
        #{'id':3,'title':'Post 3', 'content': 'Content of post 3'},
        #{'id':4,'title':'Post 4', 'content': 'Content of post 4'},
        #{'id':5,'title':'Post 5', 'content': 'Content of post 5'},
        #{'id':6,'title':'Post 6', 'content': 'Content of post 6'}
    #]

def index(request):
    techblog_title = "Latest Tech updates"
    
    # Getting data from post model
    all_posts = Post.objects.all()

    # Paginating
    paginator = Paginator(all_posts,5)
    page_no = request.GET.get('page')
    page_object = paginator.get_page(page_no)

    return render(request,'techblog/index.html',{"techblog_title": techblog_title, "page_object": page_object })

def detial(request,slug):
    # For static data
    # post = next((item for item in posts if item['id'] == int(post_id)),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')

    # Getting data from model by post id

    try:
        post = Post.objects.get(slug = slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404('Post Does not Exist!')

    return render(request,'techblog/detial.html',{'post':post,'related_posts':related_posts})

def old_url_redirect(request):
    return redirect(reverse('techblog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is new url")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            #send email or save in database
            success_message = 'Your Email has been sent!'
            return render(request,'techblog/contact.html', {'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,'techblog/contact.html', {'form':form, 'name': name, 'email':email, 'message': message})
    return render(request,'techblog/contact.html')

def about_view(request):
    about_content = Aboutus.objects.first().content
    return render(request,'techblog/about.html',{'about_content':about_content})
