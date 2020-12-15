from django.db import models
from django.utils import timezone
from django.conf import settings
from tinymce.models import HTMLField
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
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class blogpost(models.Model):
    slug = models.SlugField(verbose_name='Permalink', max_length=50, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author')
    name = models.CharField(max_length=127, verbose_name='Post title')
    description = models.TextField(max_length=24000, verbose_name='Post description', blank=True)
    desc = HTMLField(verbose_name='TinyMce Editor', blank=True)
    cover = models.ImageField(
        upload_to='blog/covers/', verbose_name='Post cover image', max_length=200, blank=True
    )
    videolink = models.URLField(default='', verbose_name='Post video cover', blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Post created Date/time')
    status = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey(
        blogcategories,
        verbose_name='category',
        on_delete=models.CASCADE,
        blank=True,
        related_name='blogpost',
    )

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'