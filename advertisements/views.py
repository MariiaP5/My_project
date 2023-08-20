from django.shortcuts import render
# получает запросы и отдает ответы
from django.http import HttpResponse # класс для ответа в формате html


# функция или классы, которые будут принимать запрос и отдавать ответ

def index(request):
    return HttpResponse("Привет")

