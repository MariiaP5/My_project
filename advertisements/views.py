from django.shortcuts import render, redirect # redirect - переадресация 
from django.urls import reverse # получение ссылки полной по название в urls
# получает запросы и отдает ответы
from django.http import HttpResponse # класс для ответа в формате html
from .forms import AdvertisementForm
from .models import Advertisement
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import get_user_model # получаем модель пользователей
from django.db.models import Count # для подсчета 
# функция или классы, которые будут принимать запрос и отдавать ответ

def index(request):
    return HttpResponse("Привет")

User = get_user_model()

# функции-представления
# <!-- {{}}  - это переменная -->
# <!-- {% %}  - это блоки с функционалом -->
# <!-- {% if else while for %}  - это блоки с функционалом -->

# render - функция для создания ответа с помощью html
def home(request: WSGIRequest):
    title = request.GET.get('query')
    if title: # если пользователь что-то ищет
        data = Advertisement.objects.filter(title__icontains = title) # SELECT * FROM Advertisement WHERE title = title
    else: # если ничего не ищет(просто все обьявления)
        data = Advertisement.objects.all() # беру все записи из БД
    context = {'advertisements' : data, 'title': title} # словарь
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
    users = User.objects.annotate(
        adv_count = Count('advertisement')# записываю в  adv_count колисчество обьявлений у каждого пользователя
    ).order_by('-adv_count') # сортировка от наибольшего к наименьшему

    context = {"users" : users}
    return render(request, 'top-sellers.html', context)

def post_adv_detail(request: WSGIRequest, pk):
    # post_adv/<int:pk>/
    # http://127.0.0.1:8000/post_adv/1/
    # pk = 1
    adv = Advertisement.objects.get(id = pk) # ищу запись по id
    context = {"adv" : adv}
    return render(request, 'advertisement.html', context)

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