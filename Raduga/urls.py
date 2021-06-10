"""
Definition of urls for Raduga.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from datetime import datetime
import app.forms
import app.views
from django.shortcuts import render, redirect
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = [
    path('', app.views.home, name='home'),
    path('contact/', app.views.contact, name='contact'),
    path('about/', app.views.about, name='about'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', app.views.registration, name='registration'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('product/', include('product.urls', namespace='product')),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()