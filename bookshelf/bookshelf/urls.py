"""Bookshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from book.views import BooksView, BookView
from registration.views import CustomPasswordChangeView, Login
from django.conf import settings
from django.conf.urls.static import static
from book.models import Book

def get_top_books():
    books = Book.objects.order_by('-rating')[:10]
    return {'books': [books[i * 5: i * 5 + 5] for i in range(2)]}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('registration.urls')),
    path('login/', Login.as_view(template_name='login.html')),
    path('', LoginView.as_view(template_name='start page.html', extra_context=get_top_books())),
    path('', include('django.contrib.auth.urls')),
    path('books', BooksView.as_view()),
    path('books/p<page>', BooksView.as_view()),
    path('book/<id>', BookView.as_view()),
    path('user/<id>', CustomPasswordChangeView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
