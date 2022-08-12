from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from member.forms import NewUserForm
from member.models import Profile

class IndexView(TemplateView):
  template_name = 'member.html'

class RegisterView(TemplateView):
  template_name = 'register.html'
  
  def get(self, request, *args, **kwargs):
    form = NewUserForm()
    return render(request, self.template_name, {'form': form, 'kwargs': kwargs})

  def post(self, request, *args, **kwargs):
    form = NewUserForm(data=request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return HttpResponseRedirect('/')

    return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):
  template_name = 'login.html'

  def get(self, request, *args, **kwargs):
    form = AuthenticationForm()
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs):
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid:
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return HttpResponseRedirect('/')
      else:
        messages.error(request,"Invalid username or password.")
    else:
      messages.error(request,"Invalid username or password.")

class LogOutView(TemplateView):

  def get(self, request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/')

class UserProfileView(DetailView):
  model = Profile
  slug_field = 'user.username'
  slug_url_kwarg = 'user'
  template_name = 'profile_view.html'

  def get_object(self):
    object = Profile.objects.get(user=self.kwargs.get('user'))
    return object
