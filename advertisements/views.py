from django.shortcuts import render, redirect # redirect - переадресация 
from django.urls import reverse # получение ссылки полной по название в urls
# получает запросы и отдает ответы
from django.http import HttpResponse # класс для ответа в формате html
from .forms import AdvertisementForm
from .models import Advertisement
from django.core.handlers.wsgi import WSGIRequest

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

def post_adv(request: WSGIRequest):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES) # передаю данные с запроса на проверку 
        if form.is_valid(): # True/False  проверяю правильность
            # print(request.POST['title'])
            print(form.cleaned_data) # отдает словарь со всеми данными
            adv = Advertisement(**form.cleaned_data) # распаковка словаря
            adv.user = request.user # отдельно указал пользователя 
            adv.save()  # сохраняю запись
            return redirect(
                reverse('home') # переадресация на главную страницу 
            )

        else: # если неправильно
            print(form.errors) # вывожу эту ошибку


    else: # GET или другие
        form = AdvertisementForm() # пустая форма

    context = {'form' : form} # словарь
    return render(request, 'advertisement-post.html', context)
   
# you.com/user
# get - получения всех пользоватлей
# post - добавление 
# put - обновление
# delete - удаление


def top_sellers(request):
    return render(request, 'top-sellers.html')


# функции будут отдавать html
def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')



# def func(x : list):
#     x.append


# func([1,2,3,4,5])


# def f(x,y):
#     print(x,y)

# r = {'x':1, 'y':2}
# f(x = r['x'], y = r['y'])
# f(**r)