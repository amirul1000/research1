from django.shortcuts import render

# Create your views here.
from django.shortcuts import  get_object_or_404, render
# Create your views here.
from django.http import HttpResponseRedirect
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from blog.forms import ContentFrom,CommentFrom

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
#from machine.forms import MessageForm,PageFrom

from blog.models import Content,Comment
from django.core.mail import send_mail


from django.contrib import auth
from django.contrib.auth.models import User

def content_view(request):
    contents_list = Content.objects.all().order_by('-id') 
    paginator = Paginator(contents_list, 10) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contents = paginator.page(paginator.num_pages)
    contentform  = ContentFrom()    
    commentform  = CommentFrom()
    return render(request, 'content_view.html',{'contents':contents,'contentform':contentform,'commentform':commentform})

#content save
def content_save(request):
    content_form = ContentFrom(request.POST)
    if content_form.is_valid():
        content = content_form.save(commit=False)
        content.poster  = User.objects.get(pk=request.user.pk)
        content.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#comment save
def comment_save(request):
    comment_form = CommentFrom(request.POST)
    if comment_form.is_valid():    	
        comment            = comment_form.save(commit=False)
        comment.content    =  Content.objects.get(pk=request.POST.get('content_id'))  
        comment.commenter  = User.objects.get(pk=request.user.pk)
        comment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))