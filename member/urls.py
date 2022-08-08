from django.urls import path
from member.views import IndexView, RegisterView, LoginView, LogOutView

urlpatterns = [
  path('', IndexView.as_view()),
  path('register/', RegisterView.as_view()),
  path('login/', LoginView.as_view()),
  path('logout/', LogOutView.as_view()),
]