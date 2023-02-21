import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render, reverse


# Create your views here.
def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now()
    msg = f"<a href='{reverse('home')}'>На главную</a> <br> <br> Текущее время: {current_time} <br>"
    return HttpResponse(msg)


def workdir_view(request):
    filelist = []
    path = os.getcwd()
    rez = sorted(os.listdir(path))
    for n, item in enumerate(rez):
        filelist.append(item)
    all_dir_files = f"Содержимое рабочей директории: {filelist} "
    return HttpResponse(all_dir_files)
