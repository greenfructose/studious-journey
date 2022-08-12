from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator
from blog.models import Article

class IndexView(TemplateView):

  def get(self, request, *args, **kwargs):
    articles = Article.objects.all().order_by('-date_published')
    most_recent_article = articles.first()
    featured_articles = Article.objects.filter(tags__name='Featured')[:3]
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    articles_obj = paginator.get_page(page)
    return render(request, 'blog.html', context={
      'articles': articles_obj,
      'most_recent': most_recent_article,
      'featured': featured_articles
      })

class ArticleDetailView(DetailView):
  template_name = 'article_detail.html'
  model = Article

class ArticleTagList(TemplateView):
  def get(self, request, *args, **kwargs):
    articles = Article.objects.filter(tags__slug=kwargs['slug']).order_by('-date_published')
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    articles_obj = paginator.get_page(page)
    return render(request, 'article_tag.html', context={'articles': articles_obj, 'slug': kwargs['slug']})