"""demo_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include, re_path
from third.views import homepage, show_books, edit_book, delete_book, restore_book, Home
from third import views




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/<int:id>/', homepage, name="home"),  # home/lalit/
    path('home/', homepage, name="home"),
    path('show-books/',show_books , name="show_books"),
    path('edit-book/<int:pk>/', edit_book, name="edit_book"),
    path('delete-book/<int:pk>/', delete_book, name="delete_book"),
    path('restore-book/<int:pk>/', restore_book, name="restore_book"),

    # path('user-login/', views.user_login, name="user_login"),
   # cbb-view
    path('cbv-home/',Home.as_view() ),
]
