from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic import CreateView
from .forms import *
from .models import Target
'''
bootstrap быстрый сделать
'''
def index(request):
    return render(request, "main_app/main_page.html", {})


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main_app/register.html'
    success_url = reverse_lazy('login')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #c_def = self.get_user_context(title="Register")
        return dict(list(context.items()))# + list(c_def.items())
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
    

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "main_app/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #c_def = self.get_user_context(title="Enter acc")
        return dict(list(context.items()))# + list(c_def.items())
    def get_success_url(self):
        return reverse_lazy('main_screen')

def logout_user(request):
    logout(request)
    return redirect('index')

def main_screen_yo(request):
    if request.method == 'POST':
        form = AddTargetForm(request.POST)
        if form.is_valid():
            #print('сохранена цель')
            try:
                Target.objects.create(**form.cleaned_data)
                return redirect('main_screen')
            except:
                form.add_error(None, 'Error detected check')
    else:
        form = AddTargetForm()
    return render(request, "main_app/main_screen.html", {'form': form,})