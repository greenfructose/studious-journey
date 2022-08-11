from django.urls import path
from blog.views import IndexView, ArticleDetailView

urlpatterns = [
  path('', IndexView.as_view()),
  path('<int:pk>', ArticleDetailView.as_view()),
]