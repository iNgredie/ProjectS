from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'ad'
urlpatterns = [
    path('create', AdCreateView.as_view()),  # создание обьявления
    path('all', AdSortView.as_view()),  # просмотр всех объявлений
    path('update/<int:pk>', AdUpdateView.as_view()),  # PUT, DELETE
    path('detail/qv/<int:pk>', AdQuickView.as_view()),  # краткая информация по обьявлению
    path('detail/fv/<int:pk>', AdFullView.as_view()),  # полная информация по обьявлению + счетчик просмотров
    path('detail/tag', TagDetailView.as_view()),  # полный список имеющихся тегов
    path('detail/tag/filter', TagFilterView.as_view()),  # фильтрация по тегам
    path('all/filter', AdDateView.as_view()),   # /?start=2020-07-17&end=2020-07-18'
]
