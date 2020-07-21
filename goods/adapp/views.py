import django_filters
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter

from .serializers import *


# Создание обьявления
class AdCreateView(generics.CreateAPIView):
    serializer_class = AdDetailSerializer


# Изменение, удаление
class AdChangeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()


# Сортировка по цене, поиск по цене, поиск по дате создания
class AdSortView(generics.ListAPIView):

    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("content", "price", "create_at")
    ordering_fields = "price", "create_at", "tag_id"


# Краткая информация по объявлению ('id', 'title', 'price')


class AdQuickView(generics.RetrieveAPIView):
    serializer_class = AdsListSerializer
    queryset = Ad.objects.all()


# Полная информация по объявлению + счетчик просмотров
class AdFullView(generics.RetrieveAPIView):
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()

    def get_object(self):
        ad = super().get_object()
        ad.view_count += 1
        ad.save()

        self.view_count = ad.view_count
        return ad


# Полная информация по объявлению + счетчик просмотров
class TagDetailView(generics.ListAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()


class AdDateTagPriceFilter(django_filters.FilterSet):
    start = filters.DateFilter(field_name="create_at", lookup_expr="gte")
    end = filters.DateFilter(field_name="create_at", lookup_expr="lte")

    fr = django_filters.NumberFilter(field_name="tag_id", lookup_expr="gte")
    to = django_filters.NumberFilter(field_name="tag_id", lookup_expr="lte")

    price__gt = filters.NumberFilter(
        field_name="price", lookup_expr="gt", label="Minimum price"
    )

    class Meta:
        model = Ad
        fields = "start", "end", "tag_id", "price", "fr", "to"


class AdDateTagPriceView(generics.ListAPIView):
    serializer_class = AdDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Ad.objects.all()
    filter_class = AdDateTagPriceFilter
