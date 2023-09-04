from django.shortcuts import render
# получает запросы и отдает ответы
from django.http import HttpResponse # класс для ответа в формате html
from .forms import AdvertisementForm
from .models import Advertisement

# функция или классы, которые будут принимать запрос и отдавать ответ

def index(request):
    return HttpResponse("Привет")

# функции-представления
# <!-- {{}}  - это переменная -->
# <!-- {% %}  - это блоки с функционалом -->
# <!-- {% if else while for %}  - это блоки с функционалом -->

# render - функция для создания ответа с помощью html
def home(request):
    data = Advertisement.objects.all() # беру все записи из БД
    context = {'advertisements' : data} # словарь
    return render(request, 'index.html', context)

def post_adv(request):
    form=AdvertisementForm() # создаю пустую форму
    context = {'form' : form}
    return render(request, 'advertisement-post.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')


# функции будут отдавать html
def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')