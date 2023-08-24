from django.db import models

# название, цена, описание, дата создания/обновления, торг

class Advertisement(models.Model): # наследую класс Model для создания таблицы в БД
    title=models.CharField(verbose_name='Название',max_length=100) # текстовое поле
    description=models.TextField('Описание')
    price=models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction=models.BooleanField('Торг', help_text='Отметьте, возможен ли торг')
    created_at=models.DateTimeField(auto_now_add=True) # сохраняем дату создания
    updated_at=models.DateTimeField(auto_now=True) # дата будет обновляться каждый раз при изменении объявления
    

    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"


    # область для работы с таблицами
    class Meta:
        db_table='advertisements'




# from advertisements.models import Advertisement
# adv1=Advertisement(title='Машина', description='Машина новая, большая, красная', price='20000000', auction=True) # создала запись
# adv1.save() # сохраняю запись

# from django.db import connection
# connection.queries # увидеть все запросы на sql

# exit()
