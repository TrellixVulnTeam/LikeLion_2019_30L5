from django.contrib import admin
from django.urls import path
from . import views
	
urlpatterns = [
        path('<int:blog_id>/', views.detail, name='detail'),
        path('new/', views.new, name='new'),
        path('create/', views.create, name='create'),
        path('delete/<int:blog_id>/', views.delete, name='delete'),
        path('update/<int:blog_id>/', views.update, name='update'),
        path('edit/<int:blog_id>/', views.edit, name='edit'),
        path('like/<int:blog_id>/',views.post_like,name='post_like'),
        
]