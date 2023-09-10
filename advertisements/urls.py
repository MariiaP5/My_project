from django.urls import path

# импортирую свои представления

from .views import test, test2, test3, home, top_sellers, post_adv, post_adv_detail

#  маршрутизатор приложения




urlpatterns = [
    path("", home, name = 'home'), # главная страница 
    path("top_sellers/", top_sellers, name='top_sellers'), # топ продавцов 
    path("post_adv/", post_adv, name='post_adv'), # добавить обьявление
    path("post_adv/<int:pk>/", post_adv_detail, name='post_adv_detail'), # рассмотреть детально обьявление http://127.0.0.1:8000/post_adv/1/

    path("test/", test, name = 'test'), 
    path("test2/", test2, name = 'test2'), 
    path("test3/", test3, name = 'test3'), 
]   



# для того чтобы отобразить html:
# 1 создать html
# 2 создать функцию представление в views.py
# 3 создать ссылку в urls.py по которой будет вызывать эта функция