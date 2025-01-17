"""postproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home, name="home"),
    path('blog/<int:blog_id>',blogapp.views.detail,name="detail"),
    path('blog/new/',blogapp.views.new,name="new"),
    path('blog/create/',blogapp.views.create, name='create'),
    path('blog/delete/<int:blog_id>/', blogapp.views.delete, name='delete'),
    #<int:...>path 컴버터 값을 받을 때 사용하는 것. blog_id에 숫자가 있는데 그걸 받으면 실행해.
    path('blog/update/<int:blog_id>/',blogapp.views.update, name='update'),
    path('blog/edit/<int:blog_id>/',blogapp.views.edit, name='edit'),
]
