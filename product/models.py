from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

# Модель категории
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:ProductListByCategory', args=[self.slug])


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.FileField(verbose_name="Изображение товара")
    description = models.TextField(verbose_name="Краткое описание")
    content = models.TextField(verbose_name = "Полное описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Наличие")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:ProductDetail', args=[self.slug])

class Review(models.Model):
     prod = models.ForeignKey(Product, on_delete = models.CASCADE, verbose_name = "Товар")
     text = models.TextField(verbose_name = "Комментарий")
     date = models.DateTimeField(default = timezone.now, db_index = True, verbose_name = "Дата")
     author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    
     def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return 'Комментарий %s к %s' % (self.author, self.prod)
    
     class Meta:
        db_table = "Reviews" # имя таблицы для модели
        verbose_name = "Комментарий" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "Комментарии к товарам" # тоже для всех статей блога
        ordering = ["-date"] # порядок сортировки данных в модели ("-" означает по убыванию)

