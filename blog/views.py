from django.shortcuts import render, redirect
from blog.models import Blog, Comment
from blog.forms import CommentForm, BlogForm
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def blog(request):
    """Renders the blog page."""
    last = Blog.objects.order_by('-posted')[:3]
    assert isinstance(request, HttpRequest)
    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    return render(
        request,
        'blog/blog.html',
        {
        'title':'Блог',
        'last': last,
        'posts': posts, # передача списка статей в шаблон веб-страницы
        'year':datetime.now().year,
        }

)

def blogpost(request, id):
    last = Blog.objects.order_by('-posted')[:3]
    post_1 = Blog.objects.get(id=id) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=id)
    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=id) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('blog:blogpost', id=id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария
    return render(
        request,
        'blog/blogpost.html',
        {
        	'last': last,
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы добавления комментария в шаблон веб-страницы
            'year':datetime.now().year,
        }
)

def newpost(request):
    """Renders the newpost page."""
    last = Blog.objects.order_by('-posted')[:3]
    if request.method == "POST":                        #после отправки формы
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.save()
            return redirect('blog')
    else:
        blogform = BlogForm()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blog/newpost.html',
        {
            'blogform': blogform,
            'last': last,
            'year': datetime.now().year,
        }
    )
