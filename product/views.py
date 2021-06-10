from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from product.models import Category, Product, Review
from product.forms import ReviewProduct
from datetime import datetime
from django.http import HttpRequest
from django.template import RequestContext

# Страница с товарами
def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product/list.html', {
    	'title': 'Все товары',
        'category': category,
        'categories': categories,
        'products': products,
        'year':datetime.now().year,
    })

# Страница товара
def ProductDetail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    reviews = Review.objects.filter(prod=product)
    if request.method == "POST": # после отправки данных формы на сервер методом POST
       form = ReviewProduct(request.POST)
       if form.is_valid():
           comment_f = form.save(commit=False)
           comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
           comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
           comment_f.product = Product.objects.get(slug=slug) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
           comment_f.save() # сохраняем изменения после добавления полей
           return redirect('product:ProductList', slug=slug) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = ReviewProduct() # создание формы для ввода комментария
    return render(request, 'product/detail.html',
                             {
                             	'title': 'Товар',
                             	'product': product,
                                'reviews': reviews,
                                'year':datetime.now().year,
                             }
                  )
