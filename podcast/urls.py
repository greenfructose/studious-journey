from django.urls import path
from podcast.views import IndexView

urlpatterns = [
  path('', IndexView.as_view()),
]