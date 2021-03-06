from django.contrib import admin
from django.urls import include, path

from .views import *

app_name = "ad"
urlpatterns = [
    # создание обьявления
    path("create/", AdCreateView.as_view()),
    # просмотр всех объявлений, сортировка, поиск
    path("all/", AdSortView.as_view()),
    # PUT, DELETE
    path("update/<int:pk>", AdChangeView.as_view()),
    # краткая информация по обьявлению
    path("detail/qv/<int:pk>", AdQuickView.as_view()),
    # полная информация по обьявлению + счетчик просмотров
    path("detail/fv/<int:pk>", AdFullView.as_view()),
    # полный список имеющихся тегов
    path("detail/tag/", TagDetailView.as_view()),
    # фильтр по дате, тегам, цене
    path("all/filter/", AdDateTagPriceView.as_view()),
]
