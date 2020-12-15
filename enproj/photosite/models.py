from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class categories(models.Model):
    slug = models.SlugField(verbose_name='Permalink', max_length=50, unique=True)
    order = models.IntegerField(verbose_name='Order', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Title', blank=True)
    description = models.TextField(max_length=800, verbose_name='Category description', blank=True)
    cover = models.ImageField(
        upload_to='uploaded/catcovers/', verbose_name='Category cover', max_length=200, blank=True
    )

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author', default='root')
    slug = models.AutoField(primary_key=True)
    order = models.IntegerField(verbose_name='Order', null=True, blank=True)
    name = models.CharField(max_length=127, blank=True)
    description = models.TextField(max_length=800, verbose_name='Description', blank=True)
    category = models.ForeignKey(
        categories,
        verbose_name='Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='postcategory',
        default=8,
    )
    image = models.ImageField(
        upload_to='uploaded/images/', verbose_name='Image', max_length=200
    )
    videolink = models.URLField(default='', verbose_name='Video link', blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Published')
    status = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Photo item'
        verbose_name_plural = 'Photo item'


class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    description = models.TextField(max_length=400, default='', verbose_name='About me', blank=True)
    avatar = models.ImageField(
        upload_to='uploaded/avatars/', verbose_name='Profile image', max_length=200, blank=True
    )
    cover = models.ImageField(
        upload_to='uploaded/usercovers/', verbose_name='Profile cover', max_length=200, blank=True
    )
    vklink = models.URLField(default='', max_length=254, verbose_name='VK', blank=True)
    fblink = models.URLField(default='', max_length=254, verbose_name='Facebook', blank=True)
    tglink = models.URLField(default='', max_length=254, verbose_name='Telegram', blank=True)
    email = models.EmailField(default='', max_length=254, verbose_name='E-mail', blank=True)
    sitename = models.CharField(default='', max_length=127, blank=True, verbose_name='Website title')
    sitesubname = models.CharField(default='', max_length=127, blank=True, verbose_name='Website sub-title')
    icon = models.FileField(
        default='', upload_to='uploaded/favicon/', max_length=254, blank=True, verbose_name='Favicon'
    )
    logobig = models.FileField(
        default='', upload_to='uploaded/logobig/', max_length=254, blank=True, verbose_name='Retina logo'
    )
    logo = models.FileField(
        default='', upload_to='uploaded/logo/', max_length=254, blank=True, verbose_name='Logo'
    )
    copyright = models.CharField(default='', max_length=127, blank=True, verbose_name='Copyright')
    customcss = models.TextField(default='', max_length=127, blank=True, verbose_name='Custom CSS')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Global Settings'
        verbose_name_plural = 'Global Settings'


def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        user_profile = userprofile.objects.create(user=user)


post_save.connect(create_profile, sender=User)
