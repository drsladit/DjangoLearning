from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
# Create your views here.


def article_list(request):
    articles = Articles.objects.all().order_by("date")
    return render(request, 'articles/articles_list.html', {'articles_list':articles})


def article_details(request,slug):
    #return HttpResponse(slug)
    article = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})


def article_year(request):
    return HttpResponse("You got output")


def article_titles(request):
    #return HttpResponse("Your title")
    article1 = Articles.objects.all().order_by("title")
    return render(request, 'articles/articles_titles.html', {'article': article1})









