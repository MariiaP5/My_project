from django.urls import path

# импортирую свои представления
from .views import profile, login_view, logout_view, sign_in


urlpatterns = [
    path('profile/', profile, name = 'profile'),
    path('login/', login_view, name='login'), # http://127.0.0.1:8000/auth/profile/
    path('logout/', logout_view, name='logout'), # http://127.0.0.1:8000/auth/profile/
    path('sign_in/', sign_in, name='sign_in'), # http://127.0.0.1:8000/auth/sign_in/
]   



# для того чтобы отобразить html:
# 1 создать html
# 2 создать функцию представление в views.py
# 3 создать ссылку в urls.py по которой будет вызывать эта функция