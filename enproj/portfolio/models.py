from django.db import models
from django.utils import timezone
from django.conf import settings


class categories(models.Model):
    slug = models.SlugField(verbose_name='Permalink', max_length=50, unique=True)
    order = models.IntegerField(verbose_name='Order', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Title', blank=True)
    description = models.TextField(max_length=800, verbose_name='Portfolio item description', blank=True)
    status = models.BooleanField(default=True, verbose_name='Published', blank=True)
    cover = models.ImageField(
        upload_to='uploaded/portfolio/catcovers/', verbose_name='Portfolio item cover image', max_length=200, blank=True
    )

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class subcategory(models.Model):
    slug = models.SlugField(verbose_name='Permalink', max_length=50, unique=True)
    order = models.IntegerField(verbose_name='Order', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Title', blank=True)
    description = models.TextField(max_length=800, verbose_name='Category description', blank=True)
    gmap = models.BooleanField(verbose_name='Use Google Maps', blank=True, default=False)
    coords = models.CharField(verbose_name='GPS coords', blank=True, max_length=20)
    status = models.BooleanField(default=True, verbose_name='Published', blank=True)
    category = models.ForeignKey(
        categories,
        verbose_name='Portfolio item',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='category',
        default=5
    )
    cover = models.ImageField(
        upload_to='uploaded/portfolio/catcovers/', verbose_name='Cateogry cover image', max_length=200, blank=True
    )

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'sub-category'
        verbose_name_plural = 'sub-categories'


class post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author', default='root',
                               related_name='pfauthor')
    slug = models.AutoField(primary_key=True)
    order = models.IntegerField(verbose_name='Order', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Title', blank=True)
    description = models.TextField(max_length=800, verbose_name='Image post description', blank=True)
    category = models.ForeignKey(
        subcategory,
        verbose_name='Image post sub-category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='subcategory',
        default=5,
    )
    image = models.ImageField(
        upload_to='uploaded/portfolio/images/', verbose_name='Upload image', max_length=200
    )
    videolink = models.URLField(default='', verbose_name='Video link', blank=True)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Uploaded at')
    status = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'image post'
        verbose_name_plural = 'image posts'
