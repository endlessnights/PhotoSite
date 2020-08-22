from django.contrib import admin

# Register your models here.
from .models import categories, post, userprofile


@admin.register(categories)
class PublishAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'order',
        'name',
        'description',
        'cover',
    ]


@admin.register(post)
class PublishAdmin(admin.ModelAdmin):
    list_display = [
        'slug',
        'order',
        'status',
        'name',
        'category',
        'image',
        'videolink',
        'created_date',
    ]


@admin.register(userprofile)
class PublishAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'description',
        'avatar',
        'cover',
        'vklink',
        'fblink',
        'tglink',
        'email',
    ]