import json
from article.models import Article
from django.http import JsonResponse
import re
from django.core import serializers
from django.db.models import query
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View

from .models import Article
from django.contrib.auth.models import User
from website.settings import BASE_DIR
from markdown import Markdown

import logging
logger = logging.getLogger(__name__)

class Home(ListView):
    model = Article
    template_name = 'article/home.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by('-views')[:3]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jumbotron'] = Article.objects.order_by(
            'c_time').last()
        return context


class ArticleList(ListView):
    model = Article
    paginate_by = 10
    template_name = 'article/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.order_by('-c_time')


# class ArticleDetail(DetailView):
#     model = Article
#     template_name = 'article/article_detail.html'
#     context_object_name = 'article'

    # def get_queryset(self):
    #     return Article.objects.get(pk=self.kwargs['pk'])

def about_page(request):
    return render(request, 'article/about.html')


# FaV template
# def single_article_detail(request, article_id):
#     try:
#         article = Article.objects.get(pk=article_id)
#     except Article.DoesNotExist:
#         raise Http404("Article does not exist")
#     print(article.title, article.cover, "ddd")
#     return render(request, 'article/single_article.html', {'article': article})


def article_list(request):
    query_set = Article.objects.values()
    query_set = [item for item in query_set]
    query_set = json.dumps(query_set, default=str)
    return HttpResponse(query_set, content_type='application/json')


def article(request, id):

    def get_author(id):
        try:
            logger.info(f'get author id={id}')
            author_info = User.objects.filter(
                id=id).values('id', 'username', 'is_superuser','last_login')
            author_info = list(author_info)
            return author_info[0]
        except Exception as e:
            logger.error(e)
            return {}

    def markd(text): # get markdown table of content
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ]
        )
        html = md.convert(text)
        return html, md.toc

    def get_object(id):  #  返回dict类型
        try:
            logger.info(f'get article id={id}')
            article = Article.objects.get(pk=id).__dict__
            del article['_state']
            article['author'] = get_author(article['author_id'])
            del article['author_id']
            article['content'], article['toc'] = markd(article['content'])
            return article
        except Exception as e:
            logger.error(e)
            raise Http404

    article = get_object(id)
    article = json.dumps(article, default=str)
    return HttpResponse(article, content_type='application/json')


