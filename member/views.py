from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from member.forms import NewUserForm

class IndexView(TemplateView):
  template_name = 'member.html'

class RegisterView(TemplateView):
  form_class = NewUserForm
  template_name = 'register.html'
  
  def get(self, request, *args, **kwargs):
    form = self.form_class()
    return render(request, self.template_name, {'form': form, 'kwargs': kwargs})

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return HttpResponseRedirect('/')

    return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):
  form_class = AuthenticationForm
  template_name = 'login.html'

  def get(self, request, *args, **kwargs):
    form = self.form_class()
    return render(request, self.template_name, {'form': form})

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid:
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
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

  def post(self, request, *args, **kwargs):
    logout = request.POST.get('user')