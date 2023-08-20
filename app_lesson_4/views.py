from django.shortcuts import render
from django.http import HttpResponse # класс для ответа в формате html


# функция или классы, которые будут принимать запрос и отдавать ответ

def lesson(request):
    return HttpResponse("Домашка по 4 занятию")

