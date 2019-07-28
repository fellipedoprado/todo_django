"""todo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import RedirectView

from core import views as todo
from users import views as users

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='/todos/')),

    #sign up, log in and log out urls
    path('signup/', users.signup_user),
    path('login/', users.login_user),
    path('login/submit', users.login_submit),
    path('logout/', users.logout_user),

    #to-do CRUD
    path('todos/', todo.list),
    path('todo/add/', todo.add),
    path('todo/add/submit', todo.save),
    path('todo/delete/<int:todo_id>', todo.delete),
    path('todos/completed/', todo.completed),
]
