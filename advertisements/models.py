from django.db import models
from django.contrib import admin
from django.utils import timezone # для времени
from django.utils.html import format_html # для создания строки html 

from django.contrib.auth import get_user_model # метод для получения класса модели пользователей
from django.urls import reverse # получение ссылки полной по название в urls


# название, цена, описание, дата создания/обновления, торг

User=get_user_model()

class Advertisement(models.Model): # наследую класс Model для создания таблицы в БД
    title=models.CharField(verbose_name='Название',max_length=100) # текстовое поле
    description=models.TextField('Описание')
    price=models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction=models.BooleanField('Торг', help_text='Отметьте, возможен ли торг')
    created_at=models.DateTimeField(auto_now_add=True) # сохраняем дату создания
    updated_at=models.DateTimeField(auto_now=True) # дата будет обновляться каждый раз при изменении объявления
    user = models.ForeignKey(User, on_delete=models.CASCADE) # если User буджет удален то все обьявления связанные с ним тоже будут удалены
    image = models.ImageField('Изображения', upload_to='advertisements/')

    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    def get_absolute_url(self):
        # post_adv/<int:pk>/
        # post_adv/self.pk/
        return reverse("post_adv_detail", kwargs={"pk": self.pk})# pk тоже самое что и id в модели

    # область для работы с таблицами
    class Meta:
        db_table='advertisements'
 
    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date(): # проверяю, что запись была создана сегодня
            created_time =  self.created_at.time().strftime('%H:%M:%S') # (19:30:15)
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня в {}</span>",created_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')
    
    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():#проверяю что запись была создана сегодня
            updated_time =  self.updated_at.time().strftime('%H:%M:%S') # 19:30:15
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня в {}</span>",updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y at %H:%M:%S')
    
    @admin.display(description='фото')
    def photo(self):
        if self.image:#проверяю что есть картинка
           
            return format_html(
                "<img src = '{}' width='100px' heigth = '100px' ",self.image.url)
        return format_html(
                "<img src = 'http://127.0.0.1:8000/media/advertisements/no_image.jpg' width='100px' heigth = '100px' ",)

# from advertisements.models import Advertisement
# adv1=Advertisement(title='Машина', description='Машина новая, большая, красная', price='20000000', auction=True) # создала запись
# adv1.save() # сохраняю запись

# from django.db import connection
# connection.queries # увидеть все запросы на sql

# exit()


# py manage.py shell   
# from add.models import Advertisement
### WHERE
### number
# adv = Advertisement.objects.filter(price__lt = 100) # lt  <
# adv = Advertisement.objects.filter(price__gt = 100) # gt  >
# adv = Advertisement.objects.filter(price__lte = 100) # lte  <=
# adv = Advertisement.objects.filter(price__gte = 100) # gte  >=

### string
# adv = Advertisement.objects.filter(title__contains = 'мол') # ищет данную строку в названиях чувствителен к регистру ("мол" in title)
# ##работает только для английского языка
# adv = Advertisement.objects.filter(title__icontains = 'мол') # ищет данную строку в названиях не чувствителен к регистру ("мол".lower() in title.lower())


# adv = Advertisement.objects.filter(title__startswith = 'Мол') # ищет данную строку в начале названия
# adv = Advertisement.objects.filter(title__endswith = 'ко') # ищет данную строку в конце названия
# adv = Advertisement.objects.filter(title__istartswith = 'Мол') # ищет данную строку в начале названия
# adv = Advertisement.objects.filter(title__iendswith = 'ко') # ищет данную строку в конце названия

# from django.db import connection
# connection.queries