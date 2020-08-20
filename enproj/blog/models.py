from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class blogcategories(models.Model):
    slug = models.SlugField(verbose_name='Пермалинк', max_length=50, unique=True)
    order = models.IntegerField(verbose_name='Порядок', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Название категории', blank=True)
    description = models.TextField(max_length=800, verbose_name='Описание категории', blank=True)
    cover = models.ImageField(
        upload_to='uploaded/catcovers/', verbose_name='Обложка категории', max_length=200, blank=True
    )

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class blogpost(models.Model):
    slug = models.SlugField(verbose_name='Пермалинк', max_length=50, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', default='root')
    name = models.CharField(max_length=127, verbose_name='Заголовок')
    description = models.TextField(max_length=800, verbose_name='Описание', blank=True)
    cover = models.ImageField(
        upload_to='blog/covers/', verbose_name='Обложка', max_length=200
    )
    videolink = models.URLField(default='', verbose_name='Ссылка на видео', blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата/время создания')
    status = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(
        blogcategories,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='blogcategory',
    )

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'запись блога'
        verbose_name_plural = 'записи блога'