from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Название", max_length=255, editable=True)
    author = models.CharField(verbose_name="Автор", max_length=100)
    content = models.TextField(verbose_name="Описание", blank=True)
    create_at = models.DateTimeField(verbose_name="Опубликовано", auto_now_add=True)
    photo = models.ImageField(
        verbose_name="Фотография", upload_to="photos/", blank=True, null=True
    )
    price = models.IntegerField(verbose_name="Цена")
    view_count = models.IntegerField(
        verbose_name="Количество просмотров", default=0, editable=False
    )
    tag = models.ForeignKey(
        Tag, related_name="tag", on_delete=models.CASCADE, default=0
    )
