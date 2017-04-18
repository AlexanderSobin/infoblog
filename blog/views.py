from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog import models
from blog.models import Article, Comments


def home(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def show_article(request, article_id):
    comments = Comments.objects.all()
    context = {
        'comments' : comments
    }
    article = get_object_or_404(Article, id = article_id)
    return render(request, 'blog/article.html', {'article': article}, comments)