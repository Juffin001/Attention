from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic import CreateView
from .forms import *
from .models import Target
import datetime
from random import choice
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

def check_today_yo(form, today):
    return form.pub_day == today

def clean_auxiliary_data(today):
    for i in Target.objects.all():
        if i.auxiliary:
            i.delete()
        if (today - i.pub_day).days > 3 and i.is_repeat == 0:
            i.delete()

def check_day_form(form, today):
    date = form.pub_day
    difference_between_two_days = today - date
    for _ in range(difference_between_two_days.days):
        date += datetime.timedelta(days=form.repeat_every)
        if date == today:
            new_form = Target.objects.create(text=form.text, day_to_beat=today, time_to_beat=form.time_to_beat, is_done=0, is_great=form.is_great, is_repeat=form.is_repeat, repeat_every=form.repeat_every, pub_date=form.pub_date, pub_day=form.pub_day, auxiliary=1)
            new_form.save()
            return [1, new_form]
    return [0]
def settings(request):
    return render(request, "main_app/settings.html", {})

def delete_item(request, task_id):
    goodbye = Target.objects.get(pk=task_id)
    goodbye.delete()
    return redirect('main_screen')

def end_task(request, task_id):
    task_end = Target.objects.get(pk=task_id)
    task_end.is_done = 1
    task_end.save()
    return redirect('main_screen')

def main_screen_yo(request):
    today = datetime.date.today()
    clean_auxiliary_data(today)
    latest_targets_list = Target.objects.order_by("-pub_date")
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
    list_today_tasks = []
    list_tomorrow_tasks = []
    list_great_task = []
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    for i in latest_targets_list:
        today_date_yo = check_day_form(i, today)
        tomorrow_date_yo = check_day_form(i, tomorrow)
        if check_today_yo(i, today):
            list_today_tasks.append(i)
        if today_date_yo[0]:
            list_today_tasks.append(today_date_yo[1])
        if tomorrow_date_yo[0]:
            list_tomorrow_tasks.append(tomorrow_date_yo[1])
        if i.is_great:
            list_great_task.append(i)
    context = {
        'random_great_task': choice(list_great_task),
        'list_great_tasks': list_great_task,
        'form': form,
        'today_tasks': list_today_tasks,
        'tomorrow_tasks': list_tomorrow_tasks,
        'latest_targets_list': latest_targets_list,
        'today': today.strftime('%A %d %B %Y'),
        'current_time': str(datetime.datetime.now().time()),
        'tomorrow': tomorrow.strftime('%A %d %B %Y'),
        'today_co': datetime.date.today(),
        'tomorrow_co': datetime.date.today() + datetime.timedelta(days=1),
    }
    return render(request, "main_app/main_screen.html", context)