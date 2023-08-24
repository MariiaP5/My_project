from django.contrib import admin
from .models import Advertisement
# импортирую класс для подсказок
from django.db.models.query import QuerySet


# admin_class - класс для кастомизации
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'updated_date', 'created_date'] # отображение в виде таблице
    list_filter = ['auction','created_at'] # параметры фильтрации
    actions = ['make_action_as_false','make_action_as_true'] # добавляю функцию для выбранных записей
    
    # создание блоков
    fieldsets = (
        ( # блок 1
            'Общее', # название блока 
            { 
                "fields": ('title','description') # поля блока
            }
        ),
        ( # блок 2
            'Финансы', # название блока 
            { 
                "fields": ('price','auction'), # поля блока
                'classes': ['collapse'], # скрыть/показать блок
                'description':'блок финансов' # подсказка о блоке
            }
        )
    )

    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False) # обновить значение auction у выбранных записей на False
    
    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True) # обновить значение auction у выбранных записей на True


# подключаю модель
admin.site.register(Advertisement, AdvertisementAdmin)
