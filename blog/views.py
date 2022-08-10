from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from blog.models import Article

class IndexView(TemplateView):

  def get(self, request, *args, **kwargs):
    articles = Article.objects.all().order_by('-date_published')
    paginator = Paginator(articles, 25)
    page = request.GET.get('page')
    articles_obj = paginator.get_page(page)
    return render(request, 'blog.html', context={'articles': articles_obj})
