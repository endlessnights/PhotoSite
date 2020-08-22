from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class categories(models.Model):
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


class post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор', default='root')
    slug = models.SlugField(verbose_name='Пермалинк', max_length=50, unique=True)
    order = models.IntegerField(verbose_name='Порядок', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Заголовок')
    description = models.TextField(max_length=800, verbose_name='Описание', blank=True)
    category = models.ForeignKey(
        categories,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='postcategory',
        default=5
    )
    image = models.ImageField(
        upload_to='uploaded/images/', verbose_name='Изображение', max_length=200
    )
    videolink = models.URLField(default='', verbose_name='Ссылка на видео', blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата/время создания')
    status = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'фото запись'
        verbose_name_plural = 'фото записи'


class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    description = models.TextField(max_length=400, default='', verbose_name='Обо мне', blank=True)
    avatar = models.ImageField(
        upload_to='uploaded/avatars/', verbose_name='Аватар', max_length=200, blank=True
    )
    cover = models.ImageField(
        upload_to='uploaded/usercovers/', verbose_name='Обложка', max_length=200, blank=True
    )
    vklink = models.URLField(default='', max_length=254, verbose_name='VK', blank=True)
    fblink = models.URLField(default='', max_length=254, verbose_name='Facebook', blank=True)
    tglink = models.URLField(default='', max_length=254, verbose_name='Telegram', blank=True)
    email = models.EmailField(default='', max_length=254, verbose_name='E-mail', blank=True)
    sitename = models.CharField(default='', max_length=127, blank=True, verbose_name='Название сайта')
    sitesubname = models.CharField(default='', max_length=127, blank=True, verbose_name='Подзаголовок сайта')
    icon = models.FileField(
        default='', upload_to='uploaded/favicon/', max_length=254, blank=True, verbose_name='Favicon'
    )
    logobig = models.FileField(
        default='', upload_to='uploaded/logobig/', max_length=254, blank=True, verbose_name='Логотип сайта Retina'
    )
    logo = models.FileField(
        default='', upload_to='uploaded/logo/', max_length=254, blank=True, verbose_name='Логотип сайта'
    )
    copyright = models.CharField(default='', max_length=127, blank=True, verbose_name='Copyright')
    customcss = models.TextField(default='', max_length=127, blank=True, verbose_name='Кастомные CSS')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'глобальные настройки'
        verbose_name_plural = 'глобальные настройки'


def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        user_profile = userprofile.objects.create(user=user)


post_save.connect(create_profile, sender=User)
