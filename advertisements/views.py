from django.shortcuts import render
# получает запросы и отдает ответы
from django.http import HttpResponse # класс для ответа в формате html


# функция или классы, которые будут принимать запрос и отдавать ответ

def index(request):
    return HttpResponse("Привет")

# render - функция для создания ответа с помощью html
def home(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')


# функции будут отдавать html
def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')