from django.urls import path
from blog.views import IndexView, ArticleDetailView, ArticleTagList

urlpatterns = [
  path('', IndexView.as_view()),
  path('<int:pk>', ArticleDetailView.as_view()),
  path('<slug:slug>', ArticleTagList.as_view()),
]