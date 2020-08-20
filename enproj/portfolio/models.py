from django.db import models
from django.utils import timezone
from django.conf import settings


class categories(models.Model):
    slug = models.SlugField(verbose_name='Пермалинк', max_length=50, unique=True)
    order = models.IntegerField(verbose_name='Порядок', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Название категории', blank=True)
    description = models.TextField(max_length=800, verbose_name='Описание категории', blank=True)
    cover = models.ImageField(
        upload_to='uploaded/portfolio/catcovers/', verbose_name='Обложка категории', max_length=200, blank=True
    )

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class subcategory(models.Model):
    slug = models.SlugField(verbose_name='Пермалинк', max_length=50, unique=True)
    order = models.IntegerField(verbose_name='Порядок', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Название категории', blank=True)
    description = models.TextField(max_length=800, verbose_name='Описание категории', blank=True)
    category = models.ForeignKey(
        categories,
        verbose_name='категория',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='category',
        default=5
    )
    cover = models.ImageField(
        upload_to='uploaded/portfolio/catcovers/', verbose_name='Обложка категории', max_length=200, blank=True
    )

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'подкатегорию'
        verbose_name_plural = 'подкатегории'


class post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', default='root',
                               related_name='pfauthor')
    slug = models.AutoField(primary_key=True)
    order = models.IntegerField(verbose_name='Порядок', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Заголовок')
    description = models.TextField(max_length=800, verbose_name='Описание', blank=True)
    category = models.ForeignKey(
        subcategory,
        verbose_name='Под-категория',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='posts',
        default=5,
    )
    image = models.ImageField(
        upload_to='uploaded/portfolio/images/', verbose_name='Изображение', max_length=200
    )
    videolink = models.URLField(default='', verbose_name='Ссылка на видео', blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата/время загрузки')
    status = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'фото запись'
        verbose_name_plural = 'фото записи'
