from django.shortcuts import render,redirect # redirect - переадресация 
from django.urls import reverse # получение ссылки полной по название в urls
from django.core.handlers.wsgi import WSGIRequest

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required # если пользователь не авторизован перенаправляем его
from django.urls import reverse_lazy # как reverse но только ленивая функция

from .forms import UserCreationCustomForm

# Create your views here.


@login_required(login_url=reverse_lazy('login'))
def profile(request):
    return render(request,'profile.html')

def logout_view(request):
    logout(request) #делаю выход для пользователя по запросу
    return redirect(reverse('login'))

# регистрация
def sign_in(request: WSGIRequest):
    if request.method == "POST":
        form = UserCreationCustomForm(request.POST) # передаю данные с запроса на проверку 
        if form.is_valid(): # True/False  проверяю правильность
            user = form.save()
            user = authenticate( username = user.username, password = request.POST['password1'])
            login(request, user = user)# аунтентификация

            return redirect(
                reverse('profile') # переадресация на профиль 
            )

        else: # если неправильно
            print(form.errors) # вывожу эту ошибку


    else: # GET или другие
        form = UserCreationCustomForm() # пустая форма

    context = {'form' : form} # словарь
    return render(request, 'register.html', context)




def login_view(request: WSGIRequest):
    if request.method == 'POST': # пользователь авторизуется
        # извлек данные из запроса
        username = request.POST["username"]
        password = request.POST["password"]
        # проверяю что такой юзер есть( если да то получааю юзера) (идентификация)
        user = authenticate(request, username = username, password = password)
        if user is not None: # если пользователь есть
            login(request, user)# аунтентификация
            return redirect(reverse('profile'))# перенаправляем на страницу профиля
        return render(request,'login.html',{"error" : "такого пользователя нет"})#иначе неправильные данные (такого юзера нет)

    elif request.method == 'GET': # просто заходит на страницу login
        if request.user.is_authenticated: # если пользователь авторизован,то
            # ему не нужна страница входа
            return redirect(reverse('profile'))# перенаправляем на страницу профиля
        else:# иначе
            return render(request,'login.html')