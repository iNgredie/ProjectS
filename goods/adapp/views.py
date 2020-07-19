from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
import django_filters
from django_filters import rest_framework as filters


class AdCreateView(generics.CreateAPIView):   # Создание обьявления
    serializer_class = AdDetailSerializer


class AdUpdateView(generics.RetrieveUpdateDestroyAPIView):  # Изменение, удаление
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()


class AdSortView(generics.ListAPIView):  # Сортировка по цене, поиск по цене, поиск по дате создания
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('content', 'price', 'create_at')
    ordering_fields = 'price', 'create_at'


class AdQuickView(generics.RetrieveAPIView):  # Краткая информация по объявлению ('id', 'title', 'price')
    serializer_class = AdsListSerializer
    queryset = Ad.objects.all()


class AdFullView(generics.RetrieveAPIView):  # Полная информация по объявлению + счетчик просмотров
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()

    def get_object(self):
        ad = super().get_object()
        ad.view_count += 1
        ad.save()

        self.view_count = ad.view_count
        return ad


class TagDetailView(generics.ListAPIView):
    serializer_class = TagDetailSerializer
    queryset = Tag.objects.all()


class TagDetailFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        to_field_name='tags',
        queryset=Ad.objects.all()
    )

    class Meta:
        model = Ad
        fields = ['tags']


class TagFilterView(generics.ListAPIView):
    serializer_class = AdDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Ad.objects.all()
    filter_class = TagDetailFilter


class AdDateFilter(django_filters.FilterSet):
    start = filters.DateFilter(field_name="create_at", lookup_expr='gte')
    end = filters.DateFilter(field_name="create_at", lookup_expr='lte')

    class Meta:
        model = Ad
        fields = 'start', 'end'


class AdDateView(generics.ListAPIView):
    serializer_class = AdDetailSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    queryset = Ad.objects.all()
    filter_class = AdDateFilter
