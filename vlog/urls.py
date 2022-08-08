from django.urls import path
from vlog.views import IndexView

urlpatterns = [
  path('', IndexView.as_view()),
]