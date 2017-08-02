# -*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,request
from .models import Article,Category
# Create your views here.
import markdown

def index(request):
    article_list = Article.objects.all()
    bar_list = Article.objects.all()
    footer_list = Category.objects.all()
    return render(request,'blog/index.html',context={'article_list':article_list,'bar_list':bar_list,'footer_list':footer_list})

def article(request,id):
    article = get_object_or_404(Article,id = id)
    bar_list = Article.objects.all()
    footer_list = Category.objects.all()
    article.body = markdown.markdown(article.body,extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request,'blog/article.html',context={'article':article,'bar_list':bar_list,'footer_list':footer_list})

def about(request):
    bar_list = Article.objects.all()
    footer_list = Category.objects.all()
    return render(request, 'blog/about.html',context={ 'bar_list': bar_list, 'footer_list': footer_list})

def articleList(request):
    article_list = Article.objects.all()
    bar_list = Article.objects.all()
    footer_list = Category.objects.all()
    return render(request, 'blog/articlelist.html',context={'article_list': article_list, 'bar_list': bar_list, 'footer_list': footer_list})


def tags(request,tag):
    article_list = Article.objects.filter(catagory= tag)
    bar_list = Article.objects.all()
    footer_list = Category.objects.all()
    return render(request, 'blog/articlelist.html',context={'article_list': article_list, 'bar_list': bar_list, 'footer_list': footer_list})

def taglist(request):
    tag_list = Category.objects.all()
    bar_list = Article.objects.all()
    footer_list = Category.objects.all()
    return render(request, 'blog/taglist.html',context={'tag_list': tag_list, 'bar_list': bar_list, 'footer_list': footer_list})

def contact(request):
    bar_list = Article.objects.all()
    footer_list = Category.objects.all()
    return render(request, 'blog/contact.html', context={'bar_list': bar_list, 'footer_list': footer_list})
