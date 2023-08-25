"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# файл отвечает за ссылки
from django.contrib import admin
from django.urls import path
from django.conf import settings # подключил файл setting
from django.conf.urls.static import static # функция для создания ссылок для картинок
# импортирую представления
from advertisements.views import index, home, top_sellers, test1, test2
from app_lesson_4.views import lesson

# urlpatterns - хранит ссылки
# name - нужен для короткого обращения к ссылки
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('home/',index), # создаю ссылку с помощью path
    path('top-sellers/',top_sellers, name='top_sellers'),
    path('lesson_4/',lesson),
    path('test1/',test1, name='test1'),
    path('test2/',test2, name='test2'),
]


if settings.DEBUG : # если файт в разработке
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) # указал ссылку и путь к файлу медиа
