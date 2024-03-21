from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('news/', views.news_list, name='news_list'), 
    path('news/<int:pk>/', views.detail_news, name='detail_news'), 
]