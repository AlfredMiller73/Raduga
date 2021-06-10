"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from blog.models import Blog
from product.models import Product, Category

def home(request):
    """Renders the home page."""
    products = Product.objects.order_by('-created')[:4]
    categories = Category.objects.order_by('name')[:5]
    last = Blog.objects.order_by('-posted')[:2]
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'last': last,
            'products': products,
            'categories': categories,
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Магазин Радуга',
            'message':'Вас приветствует компания «Радуга»!.',
            'year':datetime.now().year,
        }
    )

def registration(request):
    """Renders the registration page."""
    if request.method == "POST": # после отправки формы
        regform = UserCreationForm(request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации

            reg_f.save() # сохраняем изменения после добавления данных

            return redirect('login') # переадресация на страницу входа после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
        'regform': regform, # передача формы в шаблон веб-страницы
        'year':datetime.now().year,
        }
)
